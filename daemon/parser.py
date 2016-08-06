import apache_log_parser
import time
from pprint import pprint

from threading import Thread
import time, sys, signal

shutdown_flag = False #used for gracefull shutdown

def sighandler(signum, frame):
    print 'signal handler called with signal: %s ' % signum
    global shutdown_flag
    shutdown_flag = True
    sys.exit()

def main(argv=None):
    signal.signal(signal.SIGTERM, sighandler) # so we can handle kill gracefully
    signal.signal(signal.SIGINT, sighandler) # so we can handle ctrl-c
    try:
        Thread(target=main_loop, args=()).start()
    except Exception, reason:
        print reason

def main_loop():
    line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    FILE_PATH = '/var/log/apache2/access.log'
    SEEK_FILE = '/app/cache/seek_cache.txt'
    f = open(FILE_PATH, 'r')
    last = 0
    try:
        sf = open(SEEK_FILE, 'r')
        last = sf.read().strip()
        last = int(last)
        sf.close()
    except:
        pass
    f.seek(last)
    try:
        while not shutdown_flag:
            line = f.readline()
            if line:
                last = f.tell()
                pprint(line_parser(line))
                print "\n------\n"
            else:
                time.sleep(1)
    except:
        print "CAUGHT"
        pass
    print "OUT"
    f.close()
    with open(SEEK_FILE, 'w+') as sf:
        print "WRITING"
        sf.write(str(last))
        sf.close()
        print "WRITTEN"
    print "BYE"

if __name__ == '__main__':
    main(sys.argv)
    while 1:  # this will force your main thread to live until you terminate it.
        time.sleep(1)

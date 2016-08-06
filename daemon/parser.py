import apache_log_parser
import time
from pprint import pprint

line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
FILE_PATH = '/var/log/apache2/access.log'
SEEK_FILE = '/app/cache/seek_cache.txt'
f = open(FILE_PATH, 'r')
sf = open(SEEK_FILE, 'r')
last = sf.read().strip()
try:
    last = int(last)
except:
    last = 0
sf.close()
f.seek(last)
try:
    while True:
        line = f.readline()
        if line:
            last = f.tell()
            pprint(line_parser(line))
            print "\n------\n"
        else:
            time.sleep(1)
except:
    pass

f.close()
with open(SEEK_FILE, 'w') as sf:
    sf.write(str(last))
    sf.close()

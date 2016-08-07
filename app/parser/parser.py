import apache_log_parser
import time
import sys
from pprint import pprint
import logging
import traceback
from pymongo import MongoClient
import os

def main(SERVER_NAME, FILE_PATH, SEEK_FILE):
    logging.basicConfig(filename='out.log',level=logging.DEBUG)
    line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"")
    # MONGODB_HOST = os.environ.get('DB_PORT_27017_TCP_ADDR', '127.0.0.1')
    client = MongoClient("mongodb://db:27017/")
    
    # client = MongoClient(MONGODB_HOST)
    db = client.secfilter1
    f = open(FILE_PATH, 'r')
    last = 0
    try:
        sf = open(SEEK_FILE, 'r')
        last = sf.read().strip()
        last = int(last)
        sf.close()
    except:
        last = 0
        pass
    f.seek(last)
    try:
        while True:
            line = f.readline()
            if line:
                last = f.tell()
                out = line_parser(line)
                out["server"] = SERVER_NAME
                out["analyzed"] = False
                # pprint(out)
                db.requests.insert_one(out)
                logging.info(last)
                logging.debug(str(out)+"\n----\n")
                with open(SEEK_FILE, 'w+') as sf:
                    sf.write(str(last))
                    sf.close()
            else:
                time.sleep(1)

    except:
        traceback.print_exc()
    finally:
        f.close()
        logging.info("BYE")

if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit('Usage: %s server_name log_path tmp_file_path' % sys.argv[0])
    main(sys.argv[1],sys.argv[2],sys.argv[3])

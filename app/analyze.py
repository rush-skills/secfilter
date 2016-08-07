import logging
from pymongo import MongoClient

def analyze(request):
    # print request
    pass

def main():
    logging.basicConfig(filename='out2.log',level=logging.DEBUG)
    client = MongoClient()
    db = client.secfilter1.requests
    try:
        while True:
            requests = db.find({"analyzed":{"$eq": False}})
            if requests:
                for request in requests:
                    analyze(request)
            else:
                time.sleep(1)
    finally:
        logging.info("BYE")

if __name__ == '__main__':
    main()

import logging
from pymongo import *
from bson import *
import traceback
from attacks import check_attack

def main():
    logging.basicConfig(filename='out2.log',level=logging.DEBUG)
    client = MongoClient()
    db = client.secfilter1.requests
    threats = client.secfilter1.threats
    def insert_attack(attack, request):
        out = {
            "ip": request['remote_host'],
            "time": request['time_received_isoformat'],
            "attack": attack,
            "host": request['server'],
            "url": request['request_url'],
            "request": dbref.DBRef("requests",request)
        }
        threats.insert_one(out)
    try:
        while True:
            requests = db.find({"analyzed":{"$eq": False}})
            if requests:
                for request in requests:
                    # logging.info(request)
                    attack = check_attack(request)
                    if attack:
                        insert_attack(attack, request)
                    db.update_one({
                        "_id":request['_id']
                    },{
                        "$set": {
                            "analyzed": True
                        }
                    })
            else:
                time.sleep(1)
    except:
        traceback.print_exc()
    finally:
        logging.info("BYE")

if __name__ == '__main__':
    main()

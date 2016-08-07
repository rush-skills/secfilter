import logging
from pymongo import *
from bson import *
import traceback

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
                    attack = None
                    if request["request_header_user_agent"] == "curl/7.43.0":
                        attack = "User-Agent: curl"
                        insert_attack(attack, request)
                    if len(request["request_url_query"]) > 0:
                        attack = "Unexpected Format String"
                        insert_attack(attack, request)
                    if len(request["request_header_referer"]) > 1:
                        attack = "Unexpected Referer"
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

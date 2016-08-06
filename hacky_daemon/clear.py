from pymongo import MongoClient
client = MongoClient()
client.drop_database('secfilter1')

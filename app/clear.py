from pymongo import MongoClient
client = MongoClient()
client.drop_database('secfilter1')
with open("../shared/cache1/seek_cache.txt", 'w+') as sf:
    sf.write("0")
    sf.close()
with open("../shared/cache2/seek_cache.txt", 'w+') as sf:
    sf.write("0")
    sf.close()
with open("out.log", 'w+') as sf:
    sf.write("")
    sf.close()

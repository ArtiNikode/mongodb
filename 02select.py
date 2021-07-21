from pymongo import MongoClient

try:
    client=MongoClient("mongodb://localhost:27017")
    db=client["office"]
    coll=db["workers"]
    
    for doc in coll.find():
        print(doc)
        
except:
    print('Error...')
from pymongo import MongoClient

try:
    client=MongoClient("mongodb://localhost:27017")
    db=client["office"]
    coll=db["workers"]

    id=int(input('Enter id : '))
    qr={}
    qr["_id"]=id

    for doc in coll.find(qr):
        print(doc)
except:
    print("Error")

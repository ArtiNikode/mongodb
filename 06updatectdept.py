from pymongo import MongoClient

try:
    client=MongoClient("mongodb://localhost:27017")
    db=client["office"]
    coll=db["workers"]

    qr={}
    id=int(input('Enter ID : '))
    qr["_id"]=id
    
    upval={}
    colmn1=input('Enter new city  : ')
    colnm2=input('Enter new department: ')

    upval["city"]=colmn1
    upval["dept"]=colnm2

    upd={"$set":upval}

    coll.update_one(qr,upd)
    print("City and Department updated successfully......")


except:
    print("Error")
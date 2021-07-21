from pymongo import MongoClient

try:
    client=MongoClient("mongodb://localhost:27017")
    db=client["office"]
    coll=db["workers"]

    qr={}
    empid=int(input('Enter ID : '))
    #salary=int(input('Enter new salary: '))
    qr["_id"]=empid
    #qr["salary"]=salary

    upval={}
    colmn=int(input('Enter new salary : '))
    upval["salary"]=colmn

    upd={"$set":upval}

    coll.update_one(qr,upd)

    for doc in coll.find(qr):
        print(doc)

    print("Employee Salary updated successfully......")

except:
    print("Error")
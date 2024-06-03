import pymongo

if __name__ == "__main__":
    print("welcome to mongodb")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["lalit"]
    connection = db["myconnection"]

    rec = {"name":"lalit"}
    
    #delete only one data at one time
    connection.delete_one(rec)

    #delete all same name data at once 

    up = connection.delete_many(rec)
    #countt the deleted data 
    print(up.deleted_count)
import pymongo

if __name__ == "__main__":
    print("welcome to mongodb")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["lalit"]
    connection = db["myconnection"]

    per = {"name":"lalit"}
    nextt = {"$set": {"Location": "Pune"}}
    #for single update
    # connection = connection.update_one(per, nextt)

    #for update_manny
    up = connection = connection.update_many(per, nextt)
    print(up.modified_count)
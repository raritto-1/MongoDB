import pymongo

if __name__ == "__main__":
    print("welcome to mongodb")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["lalit"]
    connection = db["myconnection"]

    #find_one
    one = connection.find_one({"_id": 1})
    print(one)

    #find_all

    all_doc = connection.find({"Location": "Jaipur"})
    for i in all_doc:
        print(i)  
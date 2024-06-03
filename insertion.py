import pymongo

if __name__ == "__main__":
    print("welcome to mongodb")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db = client["lalit"]#database
    connection = db["myconnection"]#my_connection_Database
    dictionary = {"name":"lalit", "age" : 39}

    #insert_one
    connection.insert_one(dictionary)



    #insert_many_data

    insert_data = [{"_id": 1 ,"name":"lalit", "Location": "Jaipur"},
                    {"_id": 2 ,"name" : "pankaj", "Location" : "UP"},
                    {"_id": 3 ,"name": "rahul", "Location": "Delhi"}]

    connection.insert_many(insert_data)


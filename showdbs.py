import pymongo

if __name__ == "__main__":
    print("welcome to mongodb")

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    alldatabase = client.list_database_names()
    print(alldatabase)
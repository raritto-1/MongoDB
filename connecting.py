import pymongo

if __name__ == "__main__":
    print("Welcome to MongoDB")
    

    client = pymongo.MongoClient("mongodb://localhost:27017")
    print("Connected to MongoDB server:", client)
    


from pymongo.mongo_client import MongoClient

uri = "mongodb://localhost:27017"

client = MongoClient(uri)
dbs = client["Employees"]
collection = dbs["HR"]


def create(data):
    response = collection.insert_one(data)
    return response.inserted_id


def all():
    response = collection.find({})
    return list(response)


def get_one():
    response = collection.find_one()
    return response


def update(name):
    response = collection.update_one({"name": name}, {"$set": {"designation": "senior"}})
    return response.modified_count


def delete(name):
    response = collection.delete_one({"name": name})
    return response.deleted_count

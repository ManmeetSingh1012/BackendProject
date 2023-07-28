# This is a sample Python script.
import pymongo
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from fastapi import FastAPI
import db
import modal

app = FastAPI()

from pymongo.mongo_client import MongoClient

uri = "mongodb://localhost:27017"

client = MongoClient(uri)
dbs = client["Employees"]
collection = dbs["HR"]


@app.get("/")
def root():
    return {"message": "Welcome to mongodb"}


@app.get("/one/{name}")
def get_one(name: str):
    response = collection.find_one({"name": name})
    response["_id"] = str(response["_id"])
    print(response)
    return {"data": response}


@app.get("/all")
def get_all():
    response = db.all()
    data = []
    for i in response:
        i["_id"] = str(i["_id"])
        data.append(i)
    print(response)
    return {"data": data}


@app.delete("/delete/{name}")
def get_all(name: str):
    response = db.delete(name)
    print(response)
    return {"deleted": True, "count": response}


@app.put("/update/{name}")
def get_all(name: str):
    response = db.update(name)
    print(response)
    return {"deleted": True, "count": response}


@app.post("/create")
def create(data: modal.Todo):
    data = dict(data)
    id = str(db.create(data))
    return {"inserted ": True, "id": id}

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

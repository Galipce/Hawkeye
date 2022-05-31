from pymongo import MongoClient
from elasticsearch import Elasticsearch, helpers
import pymongo
import configparser
import os
import json

with open("Hawkeye.json") as Hawkeye:
  verilerimiz=json.load(Hawkeye)

myclient = pymongo.MongoClient(verilerimiz["ConnectingURL"])

mydb = myclient [verilerimiz["DBName"]]
user_table = mydb[verilerimiz["CollectionName"]]

ELASTIC_PASSWORD = "LqnkO92KerWSyBTewZfB8KSI"

CLOUD_ID = "Hawkeye:dXMtY2VudHJhbDEuZ2NwLmNsb3VkLmVzLmlvJGVhNDljNjZjNTMxMDQ0YzVhZjg2N2Q0ZDBhMGFjM2Y4JDk1MWNiYjYxODg4ODQ2NDY5MTUzZTQ5OTE3MDJkNDE3"


client = Elasticsearch(
    cloud_id=CLOUD_ID,
    basic_auth=("elastic", ELASTIC_PASSWORD)
)

client.info()

print("Starting to watch")
with mydb.watch(max_await_time_ms=30000) as change_stream:
    while change_stream.alive:
        print("waiting for a change")
        change = change_stream.try_next()

        if not change:
            continue

     
        print(change)

def migrate():
    res = change.find()
    # number of docs to migrate
    num_docs = 2000
    action = []
    for i in range(num_docs):
        doc = res[i]
        mongo_id = doc['_id']
        doc.pop('_id', None)
        action.append({
            "_index": client,
            "_id": mongo_id,
            "_source": json.dumps(doc)
        })
    helpers.bulk(client.actions)

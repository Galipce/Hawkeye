from pymongo import MongoClient
from elasticsearch import Elasticsearch, helpers
import configparser
import os
import json

#MongoDB Connection
client = MongoClient(os.environ["mongodb+srv://admin:admin@changestream.bddxv.mongodb.net/test?authSource=admin&replicaSet=atlas-wmd1av-shard-0&readPreference=primary&ssl=true"])
db = client[os.environ["ChangeStreamTest"]]
collection = db[os.environ["Coll1"]]



elastic = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "Xwj*Jz9y72nC3zx8Ja=E")
)


#ElasticSearch config

#es_host = os.environ["ELASTİCSEARCH_URL"]
#es = Elasticsearch([es_host])
#es_index = os.environ["ELASTICSEARCH_INDEX"]


print("Starting to watch")
with db.watch(max_await_time_ms=30000) as change_stream:
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
            "_index": elastic,
            "_id": mongo_id,
            "_source": json.dumps(doc)
        })
    helpers.bulk(elastic.actions)
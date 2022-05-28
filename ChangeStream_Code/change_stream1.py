from pymongo import MongoClient

client = MongoClient("mongodb://localhost:8080")
db = client.ChangeStreamDB()

print("Starting to watch")
with db.watch(max_await_time_ms=30000) as change_stream:
    while change_stream.alive:
        print("waiting for a change")
        change = change_stream.try_next();

        if not change:
            continue

        print(f"resume token:{change_stream.resume.token}")
        print(change)
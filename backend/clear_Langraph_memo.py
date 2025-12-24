from pymongo import MongoClient
from app.config import DB_URI

client = MongoClient(DB_URI)
db = client["checkpointing_db"]

c1 = db["checkpoints"].delete_many({})
c2 = db["checkpoint_writes"].delete_many({})

print("checkpoints deleted:", c1.deleted_count)
print("checkpoint_writes deleted:", c2.deleted_count)

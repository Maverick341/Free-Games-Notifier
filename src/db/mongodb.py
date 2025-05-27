from pymongo import MongoClient # type: ignore
from pymongo.collection import Collection # type: ignore
from pydantic import BaseModel, Field, ValidationError
from src.config import MONGO_URI

# MongoDB connection
client = MongoClient(MONGO_URI)
db = client.get_database()
subscribers_collection: Collection = db.subscribers

# Pydantic model
class Subscriber(BaseModel):
    chat_id: int
    subscribed: bool = True

# Subscriber functions
def add_subscriber(chat_id: int) -> str:
    existing = subscribers_collection.find_one({"chat_id": chat_id})

    if existing:
        if existing.get("subscribed", False):
            return "ℹ️ You're already subscribed!"
        else:
            subscribers_collection.update_one(
                {"chat_id": chat_id},
                {"$set": {"subscribed": True}}
            )
            return "✅ Subscription reactivated!"
    else:
        try:
            subscriber = Subscriber(chat_id=chat_id)
            subscribers_collection.insert_one(subscriber.model_dump())
            return "✅ You're now subscribed!"
        except ValidationError as e:
            print(f"Validation error: {e}")
            return "❌ Subscription failed due to invalid data."

def remove_subscriber(chat_id: int) -> str:
    existing = subscribers_collection.find_one({"chat_id": chat_id})

    if not existing or not existing.get("subscribed", False):
        return "ℹ️ You're not currently subscribed."
    else:
        subscribers_collection.update_one(
            {"chat_id": chat_id},
            {"$set": {"subscribed": False}}
        )
        return "❌ You've been unsubscribed."

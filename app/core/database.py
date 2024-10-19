# app/core/database.py
from motor.motor_asyncio import AsyncIOMotorClient

client: AsyncIOMotorClient = None  # Define client at the module level

async def init_db():
    global client
    client = AsyncIOMotorClient("mongodb://localhost:27017") 
    print("Database connected!")

def get_db():
    if client is None:
        raise Exception("Database not initialized. Call init_db first.")
    return client["todo_db"]

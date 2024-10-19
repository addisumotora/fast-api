from app.core.database import get_db
from app.models.todo import ToDoInDB

db = get_db()

async def create_todo(todo_data: dict):
    new_todo = ToDoInDB(**todo_data)
    result = await db["todos"].insert_one(new_todo.dict())
    return str(result.inserted_id)

async def get_todos():
    todos = await db["todos"].find().to_list(100)
    return todos

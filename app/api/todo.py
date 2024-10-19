from typing import List
from fastapi import APIRouter, HTTPException, Depends
from app.schemas.todo import ToDoCreate, ToDoResponse
from app.services.todo_service import create_todo, get_todos

todo_router = APIRouter()

@todo_router.post("/", response_model=ToDoResponse)
async def create_todo_route(todo: ToDoCreate):
    todo_id = await create_todo(todo.dict())
    return {"id": todo_id}

@todo_router.get("/", response_model=List[ToDoResponse])
async def get_all_todos():
    todos = await get_todos()
    return todos

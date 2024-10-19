from fastapi import FastAPI
from app.core.database import init_db
from app.api.todo import todo_router

app = FastAPI()

@app.lifespan("startup")
async def startup_event():
    await init_db()

app.include_router(todo_router, prefix="/api/v1/todo", tags=["ToDos"])

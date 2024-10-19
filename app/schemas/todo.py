from pydantic import BaseModel
from typing import Optional

class ToDoCreate(BaseModel):
    title: str
    description: Optional[str] = None

class ToDoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ToDoInDB(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False
    created_at: datetime = datetime.utcnow()

    class Config:
        orm_mode = True

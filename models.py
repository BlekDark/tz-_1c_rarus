from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    title: str
    priority: str

class TaskUpdate(BaseModel):
    title: Optional[str]
    priority: Optional[str]
    status: Optional[str]

class TaskOut(BaseModel):
    id: int
    title: str
    priority: str
    status: str

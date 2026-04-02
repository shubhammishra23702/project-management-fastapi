from typing import Optional
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    status: str
    project_id: int


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    status: Optional[str] = None
    project_id: Optional[int] = None
    
class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    project_id: int

    class Config:
        from_attributes = True
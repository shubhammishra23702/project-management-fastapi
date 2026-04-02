from typing import Optional
from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    owner_id: int  # ID of the user who owns the project

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    owner_id: Optional[int] = None

class ProjectResponse(BaseModel):
    id: int
    name: str
    owner_id: int

    class Config:
        from_attributes = True  # Needed to read ORM objects
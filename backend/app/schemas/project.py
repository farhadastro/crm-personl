from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProjectBase(BaseModel):
    name: str
    order_id: int

class ProjectCreate(ProjectBase):
    pass

class ProjectStatusUpdate(BaseModel):
    status: str

class Project(ProjectBase):
    id: int
    status: str
    last_activity: datetime

    class Config:
        from_attributes = True

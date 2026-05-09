from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ProjectStatusUpdate(BaseModel):
    status: str

class ProjectBase(BaseModel):
    name: str
    order_id: int

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    status: str
    last_activity: datetime

    class Config:
        from_attributes = True

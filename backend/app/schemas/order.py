from pydantic import BaseModel
from datetime import datetime

class OrderBase(BaseModel):
    client_id: int
    service_id: int
    tech_stack: str
    dataset_size: str
    deadline: datetime
    model_type: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    status: str

    class Config:
        from_attributes = True

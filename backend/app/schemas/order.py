from pydantic import BaseModel
from typing import Optional

class OrderBase(BaseModel):
    client_id: int
    service_id: int
    tech_stack: str
    dataset_size: str
    deadline: str
    model_type: str

class OrderCreate(OrderBase):
    pass

class Order(OrderBase):
    id: int
    status: str

    class Config:
        from_attributes = True

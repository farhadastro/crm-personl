from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, session
from app.schemas import order

router = APIRouter()

@router.get("/", response_model=list[order.Order])
def get_orders(db: Session = Depends(session.get_db)):
    return db.query(models.Order).all()

@router.post("/", response_model=order.Order)
def create_order(order_data: order.OrderCreate, db: Session = Depends(session.get_db)):
    new_order = models.Order(**order_data.dict())
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, session

router = APIRouter()

@router.get("/invoices")
def get_invoices(db: Session = Depends(session.get_db)):
    return db.query(models.Invoice).all()

@router.post("/invoices")
def create_invoice(order_id: int, amount: float, db: Session = Depends(session.get_db)):
    # Basic logic: create invoice from an order
    new_invoice = models.Invoice(order_id=order_id, amount=amount, status="draft")
    db.add(new_invoice)
    db.commit()
    return new_invoice

@router.patch("/invoices/{invoice_id}/status")
def update_invoice_status(invoice_id: int, status: str, db: Session = Depends(session.get_db)):
    invoice = db.query(models.Invoice).filter(models.Invoice.id == invoice_id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    invoice.status = status
    db.commit()
    return {"message": "Invoice status updated"}

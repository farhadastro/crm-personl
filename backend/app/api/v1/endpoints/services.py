from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, session
from app.core.security import admin_required

router = APIRouter()

@router.get("/services")
def get_services(db: Session = Depends(session.get_db)):
    return db.query(models.Service).filter(models.Service.is_archived == 0).all()

@router.post("/services", dependencies=[Depends(admin_required)])
def create_service(name: str, description: str, base_price: float, db: Session = Depends(session.get_db)):
    service = models.Service(name=name, description=description, base_price=base_price)
    db.add(service)
    db.commit()
    return service

@router.delete("/services/{service_id}", dependencies=[Depends(admin_required)])
def archive_service(service_id: int, db: Session = Depends(session.get_db)):
    service = db.query(models.Service).filter(models.Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    service.is_archived = 1
    db.commit()
    return {"message": "Service archived"}

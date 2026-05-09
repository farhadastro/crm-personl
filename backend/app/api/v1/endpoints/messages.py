from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import models, session
from typing import List

router = APIRouter()

@router.get("/{project_id}", response_model=List[dict])
def get_project_messages(project_id: int, db: Session = Depends(session.get_db)):
    return db.query(models.Message).filter(models.Message.project_id == project_id).all()

@router.post("/{project_id}", response_model=dict)
def create_project_message(project_id: int, content: str, db: Session = Depends(session.get_db)):
    # Assuming user_id 1 for demo purposes until auth integrated
    new_message = models.Message(project_id=project_id, sender_id=1, content=content)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return {"message": "Created", "id": new_message.id}

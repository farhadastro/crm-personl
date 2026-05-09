from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import models, session

router = APIRouter()

@router.get("/projects/{project_id}/messages")
def get_messages(project_id: int, db: Session = Depends(session.get_db)):
    return db.query(models.Message).filter(models.Message.project_id == project_id).all()

@router.post("/projects/{project_id}/messages")
def send_message(project_id: int, content: str, db: Session = Depends(session.get_db)):
    # Note: sender_id would be retrieved from JWT in real implementation
    msg = models.Message(project_id=project_id, sender_id=1, content=content)
    db.add(msg)
    db.commit()
    return {"message": "Sent"}

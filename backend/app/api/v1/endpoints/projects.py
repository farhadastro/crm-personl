from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import models, session
from app.schemas import project

router = APIRouter()

@router.get("/projects")
def get_projects(db: Session = Depends(session.get_db)):
    return db.query(models.Project).all()

@router.patch("/projects/{project_id}/status")
def update_project_status(project_id: int, status: str, db: Session = Depends(session.get_db)):
    project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    project.status = status
    db.commit()
    return {"message": "Status updated"}

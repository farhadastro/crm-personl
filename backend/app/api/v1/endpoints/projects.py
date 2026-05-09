from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import models, session
from app.schemas import project

router = APIRouter()

@router.get("/", response_model=list[project.Project])
def get_projects(db: Session = Depends(session.get_db)):
    return db.query(models.Project).all()

@router.patch("/{project_id}/status")
def update_project_status(project_id: int, update: project.ProjectStatusUpdate, db: Session = Depends(session.get_db)):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    db_project.status = update.status
    db.commit()
    db.refresh(db_project)
    return db_project

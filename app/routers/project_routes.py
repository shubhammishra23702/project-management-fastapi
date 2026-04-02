from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.connection import get_db
from app.schemas.project_schema import ProjectCreate, ProjectResponse,ProjectUpdate
from app.views.project_view import (
    create_project_view,
    get_projects_view,
    get_project_view,
    patch_project_view,
    update_project_view,
    delete_project_view
)

router = APIRouter(prefix="/projects")


@router.post("/", response_model=ProjectResponse)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project_view(project, db)


@router.get("/", response_model=list[ProjectResponse])
def get_projects(db: Session = Depends(get_db)):
    return get_projects_view(db)


@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(project_id: int, db: Session = Depends(get_db)):
    return get_project_view(project_id, db)

@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)):
    updated_project = update_project_view(project_id, project, db)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project


@router.patch("/{project_id}", response_model=ProjectResponse)
def patch_project(project_id: int, project: ProjectUpdate, db: Session = Depends(get_db)):
    updated_project = patch_project_view(project_id, project, db)
    if not updated_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project
    
@router.delete("/{project_id}", response_model=ProjectResponse)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    deleted_project = delete_project_view(project_id, db)
    if not deleted_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return deleted_project
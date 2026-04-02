from sqlalchemy.orm import Session
from app.models.project_model import Project
from app.schemas.project_schema import ProjectCreate, ProjectUpdate


def create_project_view(project: ProjectCreate, db: Session):
    new_project = Project(
        name=project.name,
        owner_id=project.owner_id
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


def get_projects_view(db: Session):
    return db.query(Project).all()


def get_project_view(project_id: int, db: Session):
    project = db.query(Project).filter(Project.id == project_id).first()
    return project

def update_project_view(project_id: int, project_data: ProjectUpdate, db: Session):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None  # Or raise HTTPException in the router

    project.name = project_data.name if project_data.name is not None else project.name
    project.owner_id = project_data.owner_id if project_data.owner_id is not None else project.owner_id

    db.commit()
    db.refresh(project)
    return project

def patch_project_view(project_id: int, project_data: ProjectUpdate, db: Session):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None  # Router will handle 404

    # Only update fields that are provided
    if project_data.name is not None:
        project.name = project_data.name
    if project_data.owner_id is not None:
        project.owner_id = project_data.owner_id

    db.commit()
    db.refresh(project)
    return project

def delete_project_view(project_id: int, db: Session):
    project = db.query(Project).filter(Project.id == project_id).first()
    if not project:
        return None  # Or raise HTTPException in the router

    db.delete(project)
    db.commit()
    return project
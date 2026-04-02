from sqlalchemy.orm import Session
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate, TaskUpdate


def create_task_view(task: TaskCreate, db: Session):
    new_task = Task(
        title=task.title,
        status=task.status,
        project_id=task.project_id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


def get_tasks_view(db: Session):
    tasks = db.query(Task).all()
    return tasks

def get_task_view(task_id: int, db: Session):
    return db.query(Task).filter(Task.id == task_id).first()


def update_task_view(task_id: int, task_data: TaskUpdate, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    task.title = task_data.title if task_data.title is not None else task.title
    task.status = task_data.status if task_data.status is not None else task.status
    task.project_id = task_data.project_id if task_data.project_id is not None else task.project_id

    db.commit()
    db.refresh(task)
    return task


def delete_task_view(task_id: int, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    db.delete(task)
    db.commit()
    return task


def patch_task_view(task_id: int, task_data: TaskUpdate, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None

    if task_data.title is not None:
        task.title = task_data.title
    if task_data.status is not None:
        task.status = task_data.status
    if task_data.project_id is not None:
        task.project_id = task_data.project_id

    db.commit()
    db.refresh(task)
    return task
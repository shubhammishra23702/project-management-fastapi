from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.connection import get_db
from app.schemas.task_schema import TaskCreate, TaskResponse, TaskUpdate
from app.views.task_view import (
    create_task_view,
    get_tasks_view,
    get_task_view,
    update_task_view,
    delete_task_view,
    patch_task_view
)

router = APIRouter()


@router.post("/tasks")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    
    create_task_view(task, db)

    return {"message": "Task created successfully"}


@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):

    tasks = get_tasks_view(db)

    return tasks

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = get_task_view(task_id, db)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated_task = update_task_view(task_id, task, db)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task


@router.delete("/{task_id}", response_model=TaskResponse)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = delete_task_view(task_id, db)
    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return deleted_task


@router.patch("/{task_id}", response_model=TaskResponse)
def patch_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    patched_task = patch_task_view(task_id, task, db)
    if not patched_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return patched_task
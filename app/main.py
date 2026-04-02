from fastapi import FastAPI
from app.utils.connection import engine, Base
from app.routers import auth_routes, project_routes, task_routes, user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_routes.router)
app.include_router(project_routes.router)
app.include_router(task_routes.router)
app.include_router(auth_routes.router)

@app.get("/")
def read_root():
    return {"message":"Welcome to the Project Management API"}
from fastapi import FastAPI
from app.routers import user, task

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.u_router)
app.include_router(task.t_router)
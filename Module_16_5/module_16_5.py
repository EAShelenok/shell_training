from fastapi import FastAPI, Path, HTTPException, status, Body, Request, Form
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel, Field
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []

class User(BaseModel):
    id: int = Field(ge=1, le=100, description="ID for User")
    username: str = Field(min_length=5, max_length=20, description="User's nickname")
    age: int = Field(ge=18, le=90, description="User's age")

@app.get("/")
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get("/users")
async def get_all_users() -> List[User]:
    return users

@app.get("/user/{user_id}")
async def get_all_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found ")

@app.post("/user/{username}/{age}")
async def create_new_user(new_user: User) -> str:
        new_user.id = max((user.id for user in users), default=0) + 1
        users.append(new_user)
        return "User is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_users(user_id: int , new_name: str, new_age: int) -> str:
    for user in users:
        if user.id == user_id:
            user.username = new_name
            user.age = new_age
            return f"The user '{user_id}' has been updated"
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    for k, user in enumerate(users):
        if user.id == user_id:
            users.pop(k)
            return f"The user {user_id} has been deleted"
    raise HTTPException(status_code=404, detail='User was not found')
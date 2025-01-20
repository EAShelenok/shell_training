from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get("/users")
async def get_all_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def create_new_user(username: Annotated[str, Path(min_length=5, max_length=20,description='Enter username',
                                                 example='UrbanUser')],
                   age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    user_id = str(int(max(users,key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_users(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='34'),
                       username: str = Path(min_length=5, max_length=20,description='Enter username',
                                            example='UrbanUser'),
                       age: int = Path(ge=18, le=120, description='Enter age', example='24')) -> str:
    if str(user_id) in users.keys():
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"The user '{user_id}' is updated"
    else:
        return f"The user with ID '{user_id}' not found. Please enter correct user ID!"

@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example='34')) -> str:
    if str(user_id) in users.keys():
        users.pop(str(user_id))
        return f"User {user_id} has been deleted"
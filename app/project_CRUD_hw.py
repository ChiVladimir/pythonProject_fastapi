from fastapi import FastAPI, Path, HTTPException
from typing import Annotated


app = FastAPI()

users = {
    '1': 'Имя: Example, возраст: 18'
         }


@app.get("/users")
async def get_all_users() -> dict:
    return users

@app.post("/user/{user_name}/{age}")
async def create_user(user_name: Annotated[str, Path(min_length=2, max_length=100, description="Enter username", example="Bob")],
        age: int = Path(ge=18, le=90, description="Enter age", example=55)) -> str:
    new_index = str(int(max(users, key=int)) + 1)
    new_user = f"Имя: {user_name}, возраст: {age}"
    users[new_index] = new_user
    return f"User {new_index} is registered"


@app.put("/user/{user_id}/{user_name}/{age}")
async def update_user(user_name: Annotated[str, Path(min_length=2, max_length=100, description="Enter username", example="Bob")],
    age: int = Path(ge=18, le=90, description="Enter age", example=55),
    user_id: int = Path(ge=0)) -> str:

    users[user_id] = f"Имя: {user_name}, возраст: {age}"
    return f"User {user_id} has been updated"

@app.delete("/user/{user_id}")
async def delete_user(user_id: int = Path(ge=0)) -> str:
    if str(user_id) in users:
        users.pop(str(user_id))
        return f"User with {user_id} was deleted."
    else:
        raise HTTPException(status_code=404, detail="user not find")




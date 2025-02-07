from fastapi import FastAPI, Path
from typing import Annotated

#rename file - uvicorn main:app --reload

app = FastAPI()

#Создайте маршрут к главной странице - "/". По нему должно выводиться сообщение "Главная страница".

@app.get("/")
async def read_root():
    return {"message": "This is the main page."}
# http://127.0.0.1:8000/

# Создайте маршрут к странице администратора - "/user/admin".
# По нему должно выводиться сообщение "Вы вошли как администратор".
@app.get("/user/admin")
async def log_adm() -> dict:
    return {"message": "You log in as administrator."}
# http://127.0.0.1:8000/user/admin

# Создайте маршрут к страницам пользователей используя параметр в пути - "/user/{user_id}".
# По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".
# @app.get("/user/{user_id}")
# async def log_user(user_id: str) -> dict:
#     return {"message": f"You log in as {user_id}"}
#http://127.0.0.1:8000/user/123

#Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".

@app.get("/user/{username}/{age}")
async def id_user(username: str
                  = Path(min_length=3, max_length=15, description="Enter your username", example="mytest")
                  ,
                  age: int
                  =Path(ge=15, le=100, description="Enter your age", example=75)
                  ) -> dict:
    return {"message": f"User Information. Username: {username}, Age: {age}"}
#http://127.0.0.1:8000/user/Ilya/24
#http://127.0.0.1:8000/user/Ilya/240
#Path дает нам возможность проверить, что к нам приходит

@app.get("/user/admin/{username}/{id}")
async def log_adm(username: Annotated[str, Path(min_length=3, max_length=15, description="Enter your username", example="mytest")]
                  , id: int) -> dict:
    return {"message": f"You log in as administrator. Dear {username}, yours ID is {id}"}
# http://127.0.0.1:8000/user/admin/Ilya/24


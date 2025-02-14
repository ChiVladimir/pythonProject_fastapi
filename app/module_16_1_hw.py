from fastapi import FastAPI

#uvicorn main:app --reload

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)

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
@app.get("/user/{user_id}")
async def log_user(user_id: str) -> dict:
    return {"message": f"You log in as {user_id}"}
#http://127.0.0.1:8000/user/123

#Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
# По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".

@app.get("/id")
async def id_user(username: str, age: int) -> dict:
    return {"message": f"User Information. Username: {username}, Age: {age}"}
#http://127.0.0.1:8000/id?username=Ilya&age=24



from fastapi import FastAPI
from pydantic import BaseModel

#rename module to main.py, run -> uvicorn main:app --reload

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

# Новый роут с предопределением (частное предопределение всегда должно быть выше)
@app.get("/user/Job/Hob")
async def news() -> dict:
    return {"message": f"Hello, mister"}
# http://127.0.0.1:8000/user/Job/Hob

#Роут с передачей параметров (передавать можно не все параметры)
@app.get("/id")
async def id_paginator(username: str = "Qq" , age: int = 25) -> dict:
    return {"User": username, "Age": age}
#http://127.0.0.1:8000/id

#Роут с запросом
@app.get("/id")
async def id_paginator(username: str, age: int) -> dict:
    return {"User": username, "Age": age}
#http://127.0.0.1:8000/id?username=Bob&age=60
#http://127.0.0.1:8000/id?age=60

#Роут с передачей параметров (передавать можно не все параметры)
@app.get("/id")
async def id_paginator(username: str = "Qq" , age: int = 25) -> dict:
    return {"User": username, "Age": age}
#http://127.0.0.1:8000/id

# новый роут
@app.get("/user/{first_name}/{last_name}")
async def news(first_name: str, last_name: str) -> dict:
    return {"message": f"Hello, {first_name} {last_name}"}
#http://127.0.0.1:8000/user/Any/Bob

# Новый роут с предопределением (частное предопределение всегда должно быть выше общего) -> Doesn't work
@app.get("/user/Job/Hob")
async def news() -> dict:
    return {"message": f"Hello, mister"}

# FastAPI поддерживает все основные HTTP-запросы: GET, POST, PUT, DELETE.
# GET-запрос — получение данных
# POST-запрос — добавление данных
# PUT-запрос — обновление данных
# DELETE-запрос — удаление данных
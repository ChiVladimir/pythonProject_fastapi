from fastapi import FastAPI
from pydantic import BaseModel

#uvicorn lesson16_1.py:app --reload

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

# новый роут
@app.get("/custom")
def read_custom_message():
    return {"message": "This is a custom message!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/items/")
async def create_item(item: Item):
    return {"name": item.name, "price": item.price}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "name": item.name, "price": item.price}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"message": "Item deleted", "item_id": item_id}

# FastAPI поддерживает все основные HTTP-запросы: GET, POST, PUT, DELETE.
# GET-запрос — получение данных
# POST-запрос — добавление данных
# PUT-запрос — обновление данных
# DELETE-запрос — удаление данных

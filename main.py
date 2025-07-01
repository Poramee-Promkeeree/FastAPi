from typing import Union

from fastapi import FastAPI, Request

from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel): 
    name: str
    price: float


@app.get("/hello")
def hello_world():
    return { "message": "Hello World 3" }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items")
def create_item(item: Item): 
    print(item.name, item.price)
    return { "request body": item }

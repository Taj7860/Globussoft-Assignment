from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# sample data
item_db = {
            1: {"name": "Laptop", "price": 75000, "is_offer": False},
            2: {"name": "Mobile", "price": 20000, "is_offer": True}
}

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool

# post api call
@app.post("/items/")
def create_item(item: Item):
    new_id = max(item_db.keys()) + 1
    item_db[new_id] = item.dict()
    return {f"New item added: {new_id}, item: {item}"}

@app.get("/item/{item_id}")
def read_item(item_id: int):
    return {f"item id: {item_id}, item detail: {item_db[item_id]}"}

@app.put("/item/{item_id}")
def update_item(item_id : int, item: Item):
    item_db[item_id] = item.dict()
    return {f"item id: {item_id}, item detail: {item_db[item_id]}"}

@app.delete("/{item_id}")
def delete_item(item_id: int):
    del_item = item_db.pop(item_id)
    return {f"item id : {item_id}, delted item: {del_item}"}
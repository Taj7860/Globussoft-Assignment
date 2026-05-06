# Update data

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool

@app.put("/item/{item_id}")
def update_item(item_id: int, item: Item):
    return {
                "item_id" : item_id,
                "updated_item" : item
    }
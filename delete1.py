from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# sample data
item_db = {
            1: {"name": "Laptop", "price": 75000, "is_offer": False},
            2: {"name": "Mobile", "price": 20000, "is_offer": True}
}

@app.delete("/{item_id}")
def delete_item(item_id: int):
    if item_id not in item_db:
        raise HTTPException(status_code = 404, details = "Item not found")
    else:
        del_item = item_db.pop(item_id)
        return del_item

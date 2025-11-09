from fastapi import FastAPI, HTTPException

from models import ItemResponse, ItemDeleteResponse, ItemListResponse, ItemUpdateResponse, Item

app = FastAPI()


@app.post("/items", response_model=ItemResponse)
def add_item(item: Item):
    pass

@app.get("/items", response_model=ItemListResponse)
def get():
    pass

@app.put("/items/{update_item_name}", response_model=ItemUpdateResponse)
def update_item(update_item_name: str, item: Item):
    pass

@app.delete("/items/{item}", response_model=ItemDeleteResponse)
def delete_item(item: str):
    pass
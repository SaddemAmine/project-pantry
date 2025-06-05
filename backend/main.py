from fastapi import FastAPI

app = FastAPI()


items = [{"id": 0, "label": "Apple"}, {"id": 1, "label": "Orange"}]

@app.get("/")
def read_root():
    return "Hello, World!"


@app.get("/items")
def get_items(item_id: int | None = None):
    if item_id:
        return items[item_id]
    return items

@app.post("/items")
def create_item(item: dict):
    item_id = len(items)
    item["id"] = item_id
    items.append(item)
    return item

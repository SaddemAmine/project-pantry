def test_create_and_list_pantry_items(client):
    item_id = client.post("/items", json={"name": "Flour"}).json()["id"]

    r = client.get("/pantry-items")
    assert r.status_code == 200 and r.json() == []

    payload = {"item_id": item_id, "quantity": 2.5, "unit": "kg"}
    r = client.post("/pantry-items", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["item_id"] == item_id
    assert body["quantity"] == 2.5

    r = client.get("/pantry-items")
    data = r.json()
    assert len(data) == 1

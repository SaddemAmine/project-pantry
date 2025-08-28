def test_create_and_list_items(client):
    r = client.get("/items")
    assert r.status_code == 200 and r.json() == []

    payload = {"name": "Apple"}
    r = client.post("/items", json=payload)
    assert r.status_code == 201
    body = r.json()
    assert body["id"] > 0
    assert body["name"] == "Apple"

    r = client.get("/items")
    assert len(r.json()) == 1

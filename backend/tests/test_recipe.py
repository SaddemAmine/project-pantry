def test_create_and_list_recipes(client):
    r = client.get("/recipes")
    assert r.status_code == 200 and r.json() == []

    payload = {"name": "Pasta", "description": "Simple", "servings": 2}
    r = client.post("/recipes", json=payload)
    assert r.status_code == 201
    rid = r.json()["id"]
    assert rid > 0

    r = client.get("/recipes")
    data = r.json()
    assert any(row["id"] == rid for row in data)

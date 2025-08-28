def test_recipe_items_and_instructions(client):
    item_id = client.post("/items", json={"name": "Tomato"}).json()["id"]
    recipe_id = client.post("/recipes", json={"name": "Salad"}).json()["id"]

    ri_payload = {"item_id": item_id, "recipe_id": recipe_id, "quantity": 3, "unit": "unit"}
    r = client.post("/recipe-items", json=ri_payload)
    assert r.status_code == 201
    ri_id = r.json()["id"]
    assert ri_id > 0

    instr_payload = {"recipe_id": recipe_id, "step_number": 1, "description": "Chop"}
    r = client.post("/recipe-instructions", json=instr_payload)
    assert r.status_code == 201
    instr_id = r.json()["id"]
    assert instr_id > 0

    assert len(client.get("/recipe-items").json()) == 1
    assert len(client.get("/recipe-instructions").json()) == 1

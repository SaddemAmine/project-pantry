def test_create_and_list_users(client):
    r = client.get("/users")
    assert r.status_code == 200 and r.json() == []

    r = client.post("/users", json={"username": "alice", "email": "a@example.com"})
    assert r.status_code == 201
    rid = r.json()["id"]
    assert rid > 0

    r = client.get("/users")
    assert any(u["id"] == rid for u in r.json())

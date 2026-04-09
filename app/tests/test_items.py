def test_create_item(client):
    response = client.post("/items/", json={"name": "Laptop", "description": "15-inch business laptop"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Laptop"

def test_create_duplicate_item(client):
    response = client.post("/items/", json={"name": "ipad", "description": "Duplicate"})
    # Should fail because name is unique
    assert response.status_code == 500 or response.status_code == 400

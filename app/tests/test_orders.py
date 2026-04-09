def test_create_order(client):
    response = client.post("/orders/", json={"item_id": 1, "vendor_id": 1, "quantity": 10})
    assert response.status_code == 200
    data = response.json()
    assert data["item_id"] == 1
    assert data["vendor_id"] == 1
    assert data["quantity"] == 10

def test_order_with_unlinked_vendor(client):
    # Try ordering with vendor_id=999 (not linked)
    response = client.post("/orders/", json={"item_id": 1, "vendor_id": 999, "quantity": 5})
    # Expect failure (depends on your validation logic)
    assert response.status_code in [400, 404]

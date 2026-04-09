def test_create_vendor(client):
    response = client.post("/vendors/", json={"name": "TechSupplier", "contact_info": "tech@supplier.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "TechSupplier"

def test_link_vendor_to_item(client):
    # Assuming item_id=1 and vendor_id=1 exist
    response = client.post("/vendors/link/1/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Vendor linked successfully"

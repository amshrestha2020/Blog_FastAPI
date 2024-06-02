def test_create_user(client):
    data = {"email":"admin@yopmail.com","password":"admin"}
    response = client.post("/users",json=data)
    assert response.status_code == 201
    assert response.json()["email"] == "admin@yopmail.com"
    assert response.json()["is_active"] == True

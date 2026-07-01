import requests

def test_update_user():
    response = requests.put(
        "https://jsonplaceholder.typicode.com/users/1",
        json={
            "id": 1,
            "name": "SHAKYA",
            "username": "shakya_updated",
            "email": "shakya@example.com"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["name"] == "SHAKYA"
    assert data["username"] == "shakya_updated"
    assert data["email"] == "shakya@example.com"
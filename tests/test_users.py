import requests

def test_get_users():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    )
    assert response.status_code == 200

def test_get_single_user():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )
    assert response.status_code == 200

def test_get_posts():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts"
    )
    assert response.status_code == 200

def test_create_post():
    data = {
        "title": "Hello",
        "body": "API Testing",
        "userId": 1
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=data
    )

    assert response.status_code == 201

def test_delete_post():
    response = requests.delete(
        "https://jsonplaceholder.typicode.com/posts/1"
    )

    assert response.status_code == 200

def test_user_name():
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1"
    )

    data = response.json()

    assert data["id"] == 1
    assert data["username"] == "Bret"

def test_update_post():
    data = {
        "id": 1,
        "title": "Updated Title",
        "body": "Updated Body",
        "userId": 1
    }

    response = requests.put(
        "https://jsonplaceholder.typicode.com/posts/1",
        json=data
    )

    assert response.status_code == 200
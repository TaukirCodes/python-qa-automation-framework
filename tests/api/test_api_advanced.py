
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_update_post_put():
    payload = {
        "id": 1,
        "title": "Updated Automation Title",
        "body": "Learning PUT API testing",
        "userId": 1
    }

    response = requests.put(
        f"{BASE_URL}/posts/1",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

    print("PUT API test passed")


def test_update_post_patch():
    payload = {
        "title": "Updated Using PATCH"
    }

    response = requests.patch(
        f"{BASE_URL}/posts/1",
        json=payload,
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["id"] == 1

    print("PATCH API test passed")


def test_delete_post():
    response = requests.delete(
        f"{BASE_URL}/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    print("DELETE API test passed")


def test_validate_post_structure(api_base_url):
    response = requests.get(
        f"{api_base_url}/posts/1",
        timeout=10
    )

    assert response.status_code == 200

    data = response.json()

    required_fields = {
        "userId",
        "id",
        "title",
        "body"
    }

    assert required_fields.issubset(data.keys())

    assert isinstance(data["userId"], int)
    assert isinstance(data["id"], int)
    assert isinstance(data["title"], str)
    assert isinstance(data["body"], str)

    assert data["id"] == 1
    assert data["title"].strip() != ""

    print("JSON structure validation passed")

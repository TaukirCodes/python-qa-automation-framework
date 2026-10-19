import requests


def test_create_post():
    url = "https://jsonplaceholder.typicode.com/posts"

    payload = {
        "title": "Automation Testing",
        "body": "Learning API automation using Python",
        "userId": 1
    }

    response = requests.post(
        url,
        json=payload,
        timeout=10
    )

    assert response.status_code == 201

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data

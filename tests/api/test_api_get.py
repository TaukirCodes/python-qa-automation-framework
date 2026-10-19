
import requests


def test_get_user():
    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["username"] == "Bret"
    assert "email" in data


def test_user_not_found():
    url = "https://jsonplaceholder.typicode.com/users/999999"

    response = requests.get(url, timeout=10)

    assert response.status_code == 404

    print("Negative API test passed")


import requests

from config.settings import API_BASE_URL
from utils.logger import get_logger


logger = get_logger(__name__)


def test_get_user():
    logger.info("Starting GET user API test")

    response = requests.get(
        f"{API_BASE_URL}/users/1",
        timeout=10
    )

    logger.info(
        "Response status: %s",
        response.status_code
    )

    assert response.status_code == 200

    data = response.json()

    assert data["id"] == 1
    assert data["username"] == "Bret"

    logger.info("GET user API test passed")

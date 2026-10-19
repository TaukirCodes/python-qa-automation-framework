
import pytest
from pages.login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("student", "Password123")

    actual = login_page.get_success_message()

    assert "Logged In Successfully" in actual


@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("wronguser", "Password123", "Your username is invalid!"),
        ("student", "wrongpass", "Your password is invalid!"),
        ("wronguser", "wrongpass", "Your username is invalid!"),
    ]
)
def test_invalid_login(driver, username, password, expected_error):
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login(username, password)

    actual = login_page.get_error_message()

    assert actual == expected_error

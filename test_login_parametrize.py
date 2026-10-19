
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL = "https://practicetestautomation.com/practice-test-login/"


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize(
    "username, password, expected_message",
    [
        ("wronguser", "Password123", "Your username is invalid!"),
        ("student", "wrongpass", "Your password is invalid!"),
        ("wronguser", "wrongpass", "Your username is invalid!"),
    ],
)
def test_invalid_login(driver, username, password, expected_message):
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located(
            (By.ID, "username")
        )
    ).send_keys(username)

    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

    error = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "error")
        )
    )

    actual_message = error.text.strip()

    assert actual_message == expected_message

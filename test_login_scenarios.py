
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


def login(driver, username, password):
    driver.get(URL)

    wait = WebDriverWait(driver, 10)

    wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    ).send_keys(username)

    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()


def test_valid_login(driver):
    login(driver, "student", "Password123")

    wait = WebDriverWait(driver, 10)

    heading = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "post-title")
        )
    )

    assert "Logged In Successfully" in heading.text


def test_invalid_username(driver):
    login(driver, "wronguser", "Password123")

    wait = WebDriverWait(driver, 10)

    error = wait.until(
        EC.visibility_of_element_located((By.ID, "error"))
    )

    assert "Your username is invalid!" in error.text


def test_invalid_password(driver):
    login(driver, "student", "wrongpass")

    wait = WebDriverWait(driver, 10)

    error = wait.until(
        EC.visibility_of_element_located((By.ID, "error"))
    )

    assert "Your password is invalid!" in error.text


def test_empty_login(driver):

    # Step 1: Submit empty credentials
    login(driver, "", "")

    # Step 2: Check the current URL
    current_url = driver.current_url

    # Step 3: Verify login was blocked
    assert "logged-in-successfully" not in current_url

    print("Empty login was blocked")


def test_empty_login(driver):
    login(driver, "", "")

    wait = WebDriverWait(driver, 10)

    error = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "error")
        )
    )

    actual_message = error.text.strip()

    print("Actual error:", actual_message)

    assert actual_message != ""
    assert "logged-in-successfully" not in driver.current_url

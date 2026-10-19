
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_valid_login():
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://practicetestautomation.com/practice-test-login/"
        )

        wait = WebDriverWait(driver, 10)

        username = wait.until(
            EC.visibility_of_element_located((By.ID, "username"))
        )
        password = driver.find_element(By.ID, "password")

        username.send_keys("student")
        password.send_keys("Password123")

        driver.find_element(By.ID, "submit").click()

        success_message = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "post-title")
            )
        )

        assert "Logged In Successfully" in success_message.text

        print("Test Passed: Login successful")

    finally:
        driver.quit()


from selenium import webdriver


def test_homepage_title():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.python.org")

        actual_title = driver.title
        expected_title = "Welcome to Python.org"

        assert actual_title == expected_title

        print("Test Passed: Homepage title is correct")

    finally:
        driver.quit()

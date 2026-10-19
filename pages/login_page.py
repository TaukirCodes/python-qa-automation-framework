from selenium.webdriver.common.by import By
from config.settings import UI_BASE_URL, DEFAULT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    URL = f"{UI_BASE_URL}/practice-test-login/"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")
    ERROR = (By.ID, "error")
    SUCCESS_HEADING = (By.CLASS_NAME, "post-title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        ).send_keys(username)

        self.driver.find_element(
            *self.PASSWORD
        ).send_keys(password)

        self.driver.find_element(
            *self.SUBMIT
        ).click()

    def get_error_message(self):
        error = self.wait.until(
            EC.visibility_of_element_located(self.ERROR)
        )
        return error.text.strip()

    def get_success_message(self):
        heading = self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_HEADING)
        )
        return heading.text.strip()


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("https://www.python.org")

    search_box = driver.find_element(By.ID, "id-search-field")

    search_box.send_keys("selenium")

    search_box.submit()

    print("Search submitted successfully")
    print("Page title:", driver.title)

finally:
    driver.quit()


import os

UI_BASE_URL = os.getenv(
    "UI_BASE_URL",
    "https://practicetestautomation.com"
)

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://jsonplaceholder.typicode.com"
)

BROWSER = os.getenv("BROWSER", "chrome")

DEFAULT_TIMEOUT = 10

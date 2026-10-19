import re
from pathlib import Path

import pytest
from selenium import webdriver


SCREENSHOT_DIR = Path("screenshots")


@pytest.fixture
def driver(request):
    browser = webdriver.Chrome()
    browser.maximize_window()

    # Store browser for the reporting hook
    request.node.driver = browser

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshots only for failed test bodies
    if report.when == "call" and report.failed:
        browser = getattr(item, "driver", None)

        if browser is not None:
            SCREENSHOT_DIR.mkdir(exist_ok=True)

            safe_name = re.sub(
                r"[^a-zA-Z0-9_-]",
                "_",
                item.nodeid
            )

            screenshot_path = (
                SCREENSHOT_DIR / f"{safe_name}.png"
            )

            try:
                browser.save_screenshot(str(screenshot_path))
                print(f"\nScreenshot saved: {screenshot_path}")
            except Exception as error:
                print(f"\nScreenshot failed: {error}")

@pytest.fixture
def api_base_url():
    return "https://jsonplaceholder.typicode.com"

def test_get_posts(api_base_url):
    response = requests.get(
        f"{api_base_url}/posts",
        timeout=10
    )

    assert response.status_code == 200
    assert isinstance(response.json(), list)
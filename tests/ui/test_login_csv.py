
import csv
from pathlib import Path

import pytest
from pages.login_page import LoginPage


DATA_FILE = (
    Path(__file__).resolve().parents[2]
    / "test_data"
    / "login_data.csv"
)


def load_test_data():
    with DATA_FILE.open(
        mode="r",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        required = {
            "test_id",
            "username",
            "password",
            "expected_error"
        }

        if not reader.fieldnames:
            raise ValueError("CSV file has no headers")

        missing = required - set(reader.fieldnames)

        if missing:
            raise ValueError(
                f"Missing CSV columns: {missing}"
            )

        return [
            pytest.param(
                row["username"],
                row["password"],
                row["expected_error"],
                id=row["test_id"]
            )
            for row in reader
        ]


@pytest.mark.parametrize(
    "username,password,expected_error",
    load_test_data()
)
def test_invalid_login_csv(
    driver, username, password, expected_error
):
    page = LoginPage(driver)

    page.open()
    page.login(username, password)

    actual_error = page.get_error_message()

    assert actual_error == expected_error


from pathlib import Path
from openpyxl import Workbook

file_path = Path("test_data/login_data.xlsx")

# Create a new Excel workbook
workbook = Workbook()

sheet = workbook.active
sheet.title = "LoginData"

# Add column headers
sheet.append([
    "test_id",
    "username",
    "password",
    "expected_error"
])

# Add test cases
test_cases = [
    ["TC_01", "wronguser", "Password123",
     "Your username is invalid!"],

    ["TC_02", "student", "wrongpass",
     "Your password is invalid!"],

    ["TC_03", "wronguser", "wrongpass",
     "Your username is invalid!"],

    ["TC_04", "student", "invalid123",
     "Your password is invalid!"]
]

for test_case in test_cases:
    sheet.append(test_case)

# Save Excel workbook
file_path.parent.mkdir(parents=True, exist_ok=True)
workbook.save(file_path)

print("Excel file created successfully!")
print("Location:", file_path.resolve())

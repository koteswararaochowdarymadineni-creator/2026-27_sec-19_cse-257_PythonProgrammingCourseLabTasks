students = {
    1: {"name": "Koti", "marks": 90},
    2: {"name": "Chowdary", "marks": 85},
    3: {"name": "Madineni", "marks": 95}
}

for roll_no, details in students.items():
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print()
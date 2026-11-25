students = [
    {"name": "Koti", "marks": 85},
    {"name": "Anu", "marks": 95},
    {"name": "Ravi", "marks": 75}
]

ascending = sorted(students, key=lambda x: x["marks"])
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("Ascending Order:")
print(ascending)

print("Descending Order:")
print(descending)
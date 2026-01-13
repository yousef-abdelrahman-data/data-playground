"""
Day 12 — Data Processing Patterns
Author: Yousef Abdelrahman

Description:
This script focuses on common data processing patterns.
It demonstrates how to:
- Treat data as rows and columns
- Filter records based on conditions
- Compute aggregated values
- Extract insights from structured data
"""
students = [
    {"name": "Yousef", "age": 22, "scores": [70, 75, 80]},
    {"name": "Andy", "age": 21, "scores": [60, 65, 70]},
    {"name": "Sandy", "age": 23, "scores": [90, 92, 88]},
]

# ----------------------------------------
# Calculate average score for each student
# ----------------------------------------
for student in students:
    total = 0

    for score in student["scores"]:
        total += score

    average = total / len(student["scores"])
    student["average"] = average   # add new column

# ----------------------------------------
# Filter high-performing students
# ----------------------------------------
print("\nHigh Performing Students:")

for student in students:
    if student["average"] >= 85:
        print(student["name"], "-", student["average"])

# ----------------------------------------
# Find overall class average
# ----------------------------------------
class_total = 0

for student in students:
    class_total += student["average"]

class_average = class_total / len(students)

print("\nClass Average:", class_average)

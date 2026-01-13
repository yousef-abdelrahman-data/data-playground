"""
Day 11 — Lists & Dictionaries Deep Dive
Author: Yousef Abdelrahman

Description:
This script focuses on working deeply with lists and dictionaries.
It demonstrates how to:
- Store structured data using a list of dictionaries
- Read values from nested data structures
- Update nested values (lists inside dictionaries)
- Treat data as rows (records) and columns (fields)
"""

# List of students (each student is a dictionary)
students = [
    {"name": "Yousef", "age": 22, "scores": [70, 75, 80]},
    {"name": "Andy", "age": 21, "scores": [60, 65, 70]},
    {"name": "Sandy", "age": 23, "scores": [90, 92, 88]},
]

# --------------------------------------------------
# Print all student names
# --------------------------------------------------
for student in students:
    print("Student name:", student["name"])

print("-" * 30)

# --------------------------------------------------
# Add a new score to each student
# (modifies the original data)
# --------------------------------------------------
for student in students:
    student["scores"].append(100)

# --------------------------------------------------
# Calculate and print average score for each student
# --------------------------------------------------
for student in students:
    total = 0

    for score in student["scores"]:
        total += score

    average = total / len(student["scores"])

    print("Student:", student["name"])
    print("Average score:", average)
    print("-" * 30)

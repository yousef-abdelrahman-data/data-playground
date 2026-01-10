"""
Day 03 — Multiple Students (List of Dictionaries)
Author: Yousef Abdelrahman

Description:
This script simulates a small dataset of multiple students.
It demonstrates how to:
- Store structured data using a list of dictionaries
- Iterate over records (rows)
- Compute averages per student
- Apply simple classification logic
"""

students = [
    {
        "name": "Yousef",
        "scores": [65, 70, 62, 80, 72]
    },
    {
        "name": "Andy",
        "scores": [65, 88, 76, 90, 60]
    },
    {
        "name": "Sandy",
        "scores": [95, 92, 88, 91, 94]
    }
]

top_student_name = ""
top_student_average = float("-inf")

for student in students:
    total = 0

    for score in student["scores"]:
        total += score

    average = total / len(student["scores"])

    print("\nStudent:", student["name"])
    print("Average:", average)

    if average >= 85:
        print("Performance: Excellent")
    elif average >= 70:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

    if average > top_student_average:
        top_student_average = average
        top_student_name = student["name"]

print("\nTop Student Summary")
print("Name:", top_student_name)
print("Average Score:", top_student_average)

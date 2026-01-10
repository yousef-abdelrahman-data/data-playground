"""
Day 03 — Multiple Students (List of Dictionaries)
Author: Yousef Abdelrahman

Description:
This script simulates a small dataset of multiple students.
It demonstrates how to:
- Store structured data using a list of dictionaries
- Iterate over records (rows)
- Compute averages per student
- Classify performance based on average score
- Identify the top-performing student
"""

# Dataset: list of students, each represented as a dictionary
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

# Track the top student's name and highest average score
top_student_name = ""
top_student_average = float("-inf")

# Iterate over each student (row)
for student in students:
    total_score = 0

    # Sum all scores for the current student
    for score in student["scores"]:
        total_score += score

    # Calculate average score
    average_score = total_score / len(student["scores"])

    # Display student results
    print("\nStudent:", student["name"])
    print("Average:", average_score)

    # Classify performance
    if average_score >= 85:
        print("Performance: Excellent")
    elif average_score >= 70:
        print("Performance: Good")
    else:
        print("Performance: Needs Improvement")

    # Update top student if current average is higher
    if average_score > top_student_average:
        top_student_average = average_score
        top_student_name = student["name"]

# Final summary of the top-performing student
print("\nTop Student Summary")
print("Name:", top_student_name)
print("Average Score:", top_student_average)

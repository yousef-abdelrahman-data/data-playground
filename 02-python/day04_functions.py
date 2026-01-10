"""
Day 04 — Functions Basics
Author: Yousef Abdelrahman

Description:
This script introduces Python functions and why they are useful.
It demonstrates how to:
- Define reusable functions
- Return values from functions
- Separate logic from presentation
"""

# ---------------------------
# Function to calculate average score
# ---------------------------
def calculate_average(scores):
    """
    Takes a list of numeric scores and returns their average.
    """
    total = 0

    for score in scores:
        total += score

    return total / len(scores)


# ---------------------------
# Function to classify performance based on average
# ---------------------------
def classify_performance(average):
    """
    Takes an average score and returns a performance label.
    """
    if average >= 85:
        return "Excellent"
    elif average >= 70:
        return "Good"
    else:
        return "Needs Improvement"


# ---------------------------
# Dataset: list of students
# ---------------------------
students = [
    {"name": "Yousef", "scores": [65, 70, 62, 80, 72]},
    {"name": "Andy", "scores": [65, 88, 76, 90, 60]},
    {"name": "Sandy", "scores": [95, 92, 88, 91, 94]},
]

# ---------------------------
# Process each student
# ---------------------------
for student in students:
    # Calculate average using function
    average = calculate_average(student["scores"])

    # Classify performance using function
    performance = classify_performance(average)

    # Output results
    print("\nStudent:", student["name"])
    print("Average:", average)
    print("Performance:", performance)

"""
Day 10 — Functions, Loops & Input Validation
Author: Yousef Abdelrahman

Description:
This script refactors a menu-driven student management system using functions.
It demonstrates how to:
- Separate logic into reusable functions
- Combine loops with function calls
- Validate user input safely
- Build cleaner and more maintainable programs
"""

# =========================
# Data storage
# =========================
students = []


# =========================
# Utility functions
# =========================
def calculate_average(scores):
    """
    Calculate the average of a list of scores.
    Returns 0 if the list is empty.
    """
    if len(scores) == 0:
        return 0

    total = 0
    for score in scores:
        total += score

    return total / len(scores)


def add_student(students):
    """
    Add a new student with validated scores.
    """
    name = input("Enter student name: ")
    scores = []

    while True:
        score_input = input("Enter score (or 'done' to finish): ")

        if score_input.lower() == "done":
            break

        try:
            score = int(score_input)

            if score < 0:
                print("Score must be a positive number.")
            else:
                scores.append(score)

        except ValueError:
            print("Invalid input. Please enter a number.")

    student = {
        "name": name,
        "scores": scores
    }

    students.append(student)
    print("Student added successfully.")


def view_students(students):
    """
    Display all stored students and their scores.
    """
    if len(students) == 0:
        print("No students found.")
        return

    for student in students:
        print("\nName:", student["name"])
        print("Scores:", student["scores"])


def show_averages(students):
    """
    Calculate and display averages and performance classification.
    """
    if len(students) == 0:
        print("No students to process.")
        return

    for student in students:
        average = calculate_average(student["scores"])

        print("\nStudent:", student["name"])
        print("Average:", average)

        if average >= 85:
            print("Performance: Excellent")
        elif average >= 70:
            print("Performance: Good")
        else:
            print("Performance: Needs Improvement")


# =========================
# Main menu loop
# =========================
while True:
    print("\nMenu:")
    print("1 - Add student")
    print("2 - View students")
    print("3 - Show averages")
    print("4 - Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student(students)
    elif choice == "2":
        view_students(students)
    elif choice == "3":
        show_averages(students)
    elif choice == "4":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")

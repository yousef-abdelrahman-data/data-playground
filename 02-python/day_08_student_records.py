"""
Day 08 — Dictionaries & Menu (Student Records)
Author: Yousef Abdelrahman

Description:
This script simulates a simple student records system.
It demonstrates how to:
- Store structured data using dictionaries
- Manage multiple records using a list
- Use a menu-driven program for interaction
- Apply loops and decision logic on records
"""

# List to store all student records
students = []

# Main program loop
while True:
    print("\nMenu:")
    print("1 - Add student")
    print("2 - View students")
    print("3 - Calculate averages")
    print("4 - Exit")

    choice = input("Choose an option: ")

    # -----------------------------------
    # Option 1: Add a new student
    # -----------------------------------
    if choice == "1":
        name = input("Enter student name: ")
        scores = []

        # Loop to collect scores for the student
        while True:
            score = input("Enter score (or 'done' to finish): ")

            if score == "done":
                break

            scores.append(int(score))

        student = {
            "name": name,
            "scores": scores
        }

        students.append(student)
        print("Student added successfully.")

    # -----------------------------------
    # Option 2: View all students
    # -----------------------------------
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print("Name:", student["name"])
                print("Scores:", student["scores"])
                print("-" * 20)

    # -----------------------------------
    # Option 3: Calculate averages
    # -----------------------------------
    elif choice == "3":
        if len(students) == 0:
            print("No students to process.")
        else:
            for student in students:
                total = 0

                for score in student["scores"]:
                    total += score

                average = total / len(student["scores"])
                print(student["name"], "average:", average)

    # -----------------------------------
    # Option 4: Exit program
    # -----------------------------------
    elif choice == "4":
        print("Exiting program...")
        break

    # -----------------------------------
    # Invalid menu choice
    # -----------------------------------
    else:
        print("Invalid choice. Please try again.")

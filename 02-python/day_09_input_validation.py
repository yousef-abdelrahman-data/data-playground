"""
Day 09 — Input Validation & Error Handling
Author: Yousef Abdelrahman

Description:
This script builds a simple student records system with input validation.
It demonstrates how to:
- Safely handle user input
- Prevent program crashes using try / except
- Validate numeric and logical conditions
- Manage structured data with lists and dictionaries
"""

# List to store all student records
students = []

# Main menu loop (runs until user exits)
while True:
    print("\nMenu:")
    print("1 - Add student")
    print("2 - View students")
    print("3 - Calculate averages")
    print("4 - Exit")

    choice = input("Choose an option: ")

    # -------------------------
    # Option 1: Add a student
    # -------------------------
    if choice == "1":
        name = input("Enter student name: ")
        scores = []

        # Loop to enter multiple scores
        while True:
            score_input = input("Enter score (or 'done' to finish): ")

            # Exit score entry loop
            if score_input.lower() == "done":
                break

            try:
                # Try converting input to integer
                score = int(score_input)

                # Validate logical correctness
                if score < 0:
                    print("Score must be positive.")
                else:
                    scores.append(score)

            except ValueError:
                # Handle non-numeric input
                print("Invalid input. Please enter a number.")

        # Create student record
        student = {
            "name": name,
            "scores": scores
        }

        students.append(student)
        print("Student added successfully.")

    # -------------------------
    # Option 2: View students
    # -------------------------
    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print("\nName:", student["name"])
                print("Scores:", student["scores"])

    # -------------------------
    # Option 3: Calculate averages
    # -------------------------
    elif choice == "3":
        if len(students) == 0:
            print("No students to process.")
        else:
            for student in students:
                if len(student["scores"]) == 0:
                    continue  # Skip students with no scores

                total = 0
                for score in student["scores"]:
                    total += score

                average = total / len(student["scores"])
                print(student["name"], "average:", average)

    # -------------------------
    # Option 4: Exit program
    # -------------------------
    elif choice == "4":
        print("Exiting program...")
        break

    # -------------------------
    # Invalid menu choice
    # -------------------------
    else:
        print("Invalid choice. Please try again.")

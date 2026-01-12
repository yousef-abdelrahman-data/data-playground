"""
Day 07 — Lists & While (Menu-Driven Program)
Author: Yousef Abdelrahman

Description:
This script demonstrates how to build a simple menu-driven program.
It shows how to:
- Store values using lists
- Use while loops for continuous execution
- Control program flow using user input
- Apply decision logic with if / elif / else
"""

# List to store scores entered by the user
scores = []

# Main program loop (runs until user chooses to exit)
while True:
    print("\nMenu:")
    print("1 - Add score")
    print("2 - View scores")
    print("3 - Calculate average")
    print("4 - Exit")

    choice = input("Choose an option: ")

    # Option 1: Add a new score
    if choice == "1":
        score = int(input("Enter score: "))
        scores.append(score)
        print("Score added successfully.")

    # Option 2: View all stored scores
    elif choice == "2":
        print("Scores:", scores)

    # Option 3: Calculate average score
    elif choice == "3":
        if len(scores) == 0:
            print("No scores available to calculate average.")
        else:
            total = 0
            for score in scores:
                total += score

            average = total / len(scores)
            print("Average score:", average)

    # Option 4: Exit the program
    elif choice == "4":
        print("Exiting program...")
        break

    # Handle invalid menu choices
    else:
        print("Invalid choice. Please try again.")

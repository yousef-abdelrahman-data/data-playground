"""
Day 06 — Loops & Control Flow
Author: Yousef Abdelrahman

Description:
This script focuses on loop mechanics and control flow.
It demonstrates how to:
- Use for and while loops
- Control loop execution using break and continue
- Combine loops with conditional logic
- Use while loops for condition-based iteration
- Control program flow using user input
"""

# -----------------------------------
# Example 1: for loop with break & continue
# -----------------------------------

for i in range(1, 10):
    if i == 5:
        print("Skipping 5")
        continue      # skip this iteration only
    elif i == 8:
        print("Stopping at 8")
        break         # exit the loop completely
    else:
        print(i)


# -----------------------------------
# Example 2: basic while loop (counter-based)
# -----------------------------------

counter = 1

while counter <= 5:
    print(counter)
    counter += 1     # move toward stopping condition


# -----------------------------------
# Example 3: infinite loop with user-controlled exit
# -----------------------------------

while True:
    user_input = input("Type something (or 'exit' to quit): ")

    if user_input == "exit":
        print("Exiting program...")
        break

    print("You typed:", user_input)


# -----------------------------------
# Example 4: input validation using while
# -----------------------------------

age = -1

while age <= 0:
    age = int(input("Please enter a valid age: "))

print("Age accepted:", age)

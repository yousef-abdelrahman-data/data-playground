"""
Day 01 - Python Basics
Author: Yousef Abdelrahman

This file covers the fundamentals of Python needed for data-related tracks:
- Variables and data types
- User input and type casting
- Conditional logic
- Loops
"""

# --------------------------------------------------
# Basic Variables
# --------------------------------------------------

name = "Yousef"
track = "Data"

print("Name:", name)
print("Track:", track)


# --------------------------------------------------
# Variables and Data Types
# --------------------------------------------------

age = 22            # Integer
gpa = 3.4           # Float
is_student = True   # Boolean

print("Age:", age, type(age))
print("GPA:", gpa, type(gpa))
print("Is student:", is_student, type(is_student))


# --------------------------------------------------
# User Input and Type Casting
# --------------------------------------------------

# input() always returns a string, so we cast it to int
user_age = input("Enter your age: ")
user_age = int(user_age)

print("Your age is:", user_age)
print("Type of age:", type(user_age))


# --------------------------------------------------
# Conditional Statements (if / else)
# --------------------------------------------------

# Basic age classification
if user_age >= 18:
    print("Adult")
else:
    print("Minor")


# --------------------------------------------------
# Extended Conditional Logic (Child / Teen / Adult)
# --------------------------------------------------

if user_age < 13:
    print("Child")
elif 13 <= user_age < 18:
    print("Teen")
else:
    print("Adult")


# --------------------------------------------------
# Loops (for)
# --------------------------------------------------

# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)


# --------------------------------------------------
# Combining Loops with Conditions (Even / Odd)
# --------------------------------------------------

# Loop from 1 to 10 and classify numbers as Even or Odd
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")

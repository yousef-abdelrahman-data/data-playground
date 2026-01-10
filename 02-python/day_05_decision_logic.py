"""
Day 05 — Decision Logic & Conditions
Author: Yousef Abdelrahman

Description:
This script focuses on decision-making using conditional logic.
It demonstrates how to:
- Use if / elif / else
- Combine conditions with logical operators
- Make decisions based on computed values
"""

# --------------------------------------------------
# Example 1: Simple decision based on a single value
# --------------------------------------------------

score = 72

if score >= 85:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Needs Improvement")


# --------------------------------------------------
# Example 2: Decision using multiple conditions
# --------------------------------------------------

age = 20
is_student = True

if age >= 18 and is_student:
    print("Adult student")
elif age >= 18 and not is_student:
    print("Adult non-student")
else:
    print("Minor")


# --------------------------------------------------
# Example 3: Decision based on combined metrics
# --------------------------------------------------

average = 82
attendance = 90

if average >= 85 and attendance >= 80:
    result = "Excellent student"
elif average >= 70 and attendance >= 60:
    result = "Good student"
else:
    result = "At risk"

print("Result:", result)

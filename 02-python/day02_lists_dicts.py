# =====================================
# Day 02 — Lists & Dictionaries Basics
# =====================================

# -----------------
# Lists Basics
# -----------------

# A list of student scores
scores = [85, 90, 78, 92, 88]

# Basic list operations
print("Scores:", scores)
print("Number of scores:", len(scores))
print("Highest score:", max(scores))
print("Lowest score:", min(scores))


# -----------------
# Looping Through a List
# -----------------

total = 0

for score in scores:
    total += score  # accumulate total score

average = total / len(scores)

print("Total:", total)
print("Average:", average)


# -----------------
# Simple Classification Logic
# -----------------

if average >= 85:
    print("Performance:", "Excellent")
elif average >= 70:
    print("Performance:", "Good")
else:
    print("Performance:", "Needs Improvement")


# -----------------
# Dictionary Basics
# -----------------

# Dictionary representing a single student
student = {
    "name": "Yousef",
    "age": 22,
    "track": "Data",
    "scores": [85, 90, 78, 92, 88]
}

# Accessing dictionary values
print("\nStudent Information")
print("Name:", student["name"])
print("Age:", student["age"])
print("Track:", student["track"])
print("Scores:", student["scores"])


# -----------------
# Processing Data Inside a Dictionary
# -----------------

total = 0

for s in student["scores"]:
    total += s

average = total / len(student["scores"])

print("Average score:", average)


# -----------------
# Final Evaluation
# -----------------

if average >= 85:
    print("Final Evaluation:", "Excellent")
elif average >= 70:
    print("Final Evaluation:", "Good")
else:
    print("Final Evaluation:", "Needs Improvement")

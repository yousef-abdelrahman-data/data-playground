# ============================================
# Data Playground – Day 13
# Topic: Strings & Data Traversal
# Track: Python → SQL → Power BI → CS50
# Author: Youssuf Abdulrahman
# ============================================

"""
Day 13 focuses on understanding strings as iterable data structures.
We practice:
- Indexing
- Slicing
- Traversing strings using loops
- Counting and searching
- Building new strings from old ones

Strings in Python are immutable:
You never change them — you create new ones.
"""

# -------- 1. Basic String Indexing --------

text = "Data Playground"

print(text[0])      # First character
print(text[-1])     # Last character
print(text[5])      # Space counts as a character

# -------- 2. String Slicing --------

print(text[0:4])    # 'Data'
print(text[5:])     # 'Playground'
print(text[:4])     # 'Data'
print(text[::2])    # Every second character

# -------- 3. Traversing a String (for loop) --------

for char in text:
    print(char)

# -------- 4. Counting Characters --------

word = "mississippi"
count = 0

for char in word:
    if char == "s":
        count += 1

print("Number of 's':", count)

# -------- 5. Searching in a String --------

email = "user@example.com"

found = False
for char in email:
    if char == "@":
        found = True
        break

print("Contains @ ?", found)

# -------- 6. Building a New String --------

original = "Data123Play456"
clean = ""

for char in original:
    if char.isalpha():
        clean += char

print(clean)  # DataPlay

# -------- 7. Reverse a String (Manual Way) --------

text = "Python"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)

text = "Python"
reversed_text = text[::-1]
print(reversed_text)  # Output: nohtyP

# -------- 8. Character Frequency (Mini Dictionary Logic) --------

sentence = "data playground"
freq = {}

for char in sentence:
    if char == " ":
        continue

    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)

# -------- 9. Traversal with Index --------

text = "SQLPowerBI"

for i in range(len(text)):
    print(f"Index {i} -> {text[i]}")

# -------- 10. Palindrome Check --------

word = "racecar"
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-(i + 1)]:
        is_palindrome = False
        break
print(f"{word} is palindrome? {is_palindrome}")
# Alternative method
is_palindrome = word == word[::-1]
print(f"{word} is palindrome? {is_palindrome}")

sentence = "nurses run"

# 1. Clean the string (remove spaces and make lowercase)
cleaned = sentence.replace(" ", "").lower()

# 2. Compare to its reverse
if cleaned == cleaned[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

# ============================================================
# End of Day 13 — Strings & Data Traversal
# ============================================================ 
# Demo for Using for and while Loops

# Loops allow you to execute code repeatedly.
# for loops iterate over sequences (lists, strings, ranges, etc.).
# while loops continue as long as a condition is true.
# Loops are essential for processing collections of data and repetitive tasks.

# for loops

# Basic for loop with range
print("Basic for loop with range:")
for i in range(5):
    print(f"Iteration {i}")
print()

# for loop with list
print("for loop with list:")
fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"I like {fruit}")
print()

# for loop with string
print("for loop with string:")
word = "Python"
for letter in word:
    print(f"Letter: {letter}")
print()

# for loop with enumerate (getting index and value)
print("for loop with enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")
print()

# for loop with dictionary
print("for loop with dictionary:")
person = {"name": "Alice", "age": 30, "city": "New York"}
for key in person:
    print(f"{key}: {person[key]}")

# Iterating over key-value pairs
for key, value in person.items():
    print(f"{key} -> {value}")
print()

# Nested for loops
print("Nested for loops:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
print()

# List comprehension (compact for loop)
print("List comprehension:")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Even squares: {even_squares}")
print()

# while loops

# Basic while loop
print("Basic while loop:")
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1
print()

# while loop with user input simulation
print("while loop with condition:")
# Simulating user input
responses = ["yes", "yes", "no"]
index = 0

while index < len(responses) and responses[index] == "yes":
    print("Continuing...")
    index += 1
print("Loop ended")
print()

# Infinite loop prevention
print("Infinite loop prevention:")
# This would be infinite without break
attempts = 0
while True:
    attempts += 1
    print(f"Attempt {attempts}")
    if attempts >= 3:
        print("Breaking out of loop")
        break
print()

# while loop with else
print("while loop with else:")
number = 5
while number > 0:
    print(f"Number: {number}")
    number -= 1
else:
    print("Loop completed normally")
print()

# Loop control statements

# break statement
print("break statement:")
for i in range(10):
    if i == 5:
        print("Breaking at 5")
        break
    print(f"Number: {i}")
print()

# continue statement
print("continue statement:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")
print()

# pass statement (placeholder)
print("pass statement:")
for i in range(3):
    if i == 1:
        pass  # Do nothing
    else:
        print(f"Processing {i}")
print()

# Practical examples

# Processing a list of numbers
print("Processing a list of numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_count += 1

print(f"Sum of even numbers: {even_sum}")
print(f"Count of odd numbers: {odd_count}")
print()

# Finding maximum value
print("Finding maximum value:")
scores = [85, 92, 78, 96, 88]
max_score = scores[0]

for score in scores[1:]:
    if score > max_score:
        max_score = score

print(f"Maximum score: {max_score}")
print()

# Data validation loop
print("Data validation loop:")
valid_data = []
raw_data = [10, "invalid", 20, None, 30, "also invalid", 40]

for item in raw_data:
    if isinstance(item, int) and item > 0:
        valid_data.append(item)

print(f"Valid data: {valid_data}")
print()

# Generating patterns
print("Generating patterns:")
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}", end="\t")
    print()  # New line
print()

# Fibonacci sequence with while
print("Fibonacci sequence:")
a, b = 0, 1
count = 0
while count < 10:
    print(f"Fibonacci {count}: {a}")
    a, b = b, a + b
    count += 1
print()

# File processing simulation
print("File processing simulation:")
# Simulating lines in a file
file_lines = ["Name: Alice", "Age: 30", "Name: Bob", "Age: 25", "Name: Charlie"]

names = []
for line in file_lines:
    if line.startswith("Name:"):
        name = line.split(": ")[1]
        names.append(name)

print(f"Extracted names: {names}")
print()

# Loop efficiency considerations
print("Loop efficiency:")
import time

# Inefficient way
start = time.time()
result = []
for i in range(1000):
    result.append(i * 2)
end = time.time()
print(f"Loop time: {end - start:.4f} seconds")

# More efficient way (list comprehension)
start = time.time()
result = [i * 2 for i in range(1000)]
end = time.time()
print(f"List comprehension time: {end - start:.4f} seconds")
print()

# Best practices
print("Best practices for loops:")
print("1. Use for loops when you know the number of iterations")
print("2. Use while loops when you need to loop until a condition is met")
print("3. Avoid infinite loops by ensuring conditions will eventually be false")
print("4. Use break and continue sparingly for clarity")
print("5. Consider list comprehensions for simple transformations")
print("6. Use meaningful variable names")
print("7. Test edge cases (empty sequences, boundary values)")

print("\nLoops demo completed!")
# Demo for Working with Python Lists, Tuples, and Dictionaries

# Python provides several built-in data structures for storing collections of data.
# Lists are mutable ordered collections.
# Tuples are immutable ordered collections.
# Dictionaries are mutable unordered collections of key-value pairs.
# These are fundamental for data manipulation in Python.

# Lists

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]

print("Creating lists:")
print(f"empty_list = {empty_list}")
print(f"numbers = {numbers}")
print(f"fruits = {fruits}")
print(f"mixed = {mixed}")
print()

# List operations
print("List operations:")
# Accessing elements
print(f"numbers[0] = {numbers[0]}")  # First element
print(f"numbers[-1] = {numbers[-1]}")  # Last element
print(f"numbers[1:4] = {numbers[1:4]}")  # Slicing

# Modifying lists (lists are mutable)
numbers.append(6)  # Add to end
print(f"After append(6): {numbers}")

numbers.insert(0, 0)  # Insert at position
print(f"After insert(0, 0): {numbers}")

numbers.remove(3)  # Remove value
print(f"After remove(3): {numbers}")

popped = numbers.pop()  # Remove and return last element
print(f"Popped: {popped}, remaining: {numbers}")

numbers.extend([7, 8])  # Add multiple elements
print(f"After extend([7, 8]): {numbers}")
print()

# List methods
sample_list = [3, 1, 4, 1, 5, 9, 2, 6]
print("List methods:")
print(f"Original: {sample_list}")
print(f"len(sample_list) = {len(sample_list)}")
print(f"sum(sample_list) = {sum(sample_list)}")
print(f"max(sample_list) = {max(sample_list)}")
print(f"min(sample_list) = {min(sample_list)}")
print(f"sorted(sample_list) = {sorted(sample_list)}")
print(f"sample_list.index(5) = {sample_list.index(5)}")
print(f"sample_list.count(1) = {sample_list.count(1)}")
print()

# Tuples

# Creating tuples
empty_tuple = ()
single_element = (42,)  # Note the comma
coordinates = (10, 20)
colors = ("red", "green", "blue")

print("Creating tuples:")
print(f"empty_tuple = {empty_tuple}")
print(f"single_element = {single_element}")
print(f"coordinates = {coordinates}")
print(f"colors = {colors}")
print()

# Tuple operations
print("Tuple operations:")
# Accessing elements (same as lists)
print(f"coordinates[0] = {coordinates[0]}")
print(f"colors[-1] = {colors[-1]}")
print(f"colors[1:3] = {colors[1:3]}")

# Tuples are immutable - these will fail
# coordinates[0] = 15  # TypeError
# colors.append("yellow")  # AttributeError

print("Tuples are immutable - cannot modify after creation")
print()

# Tuple methods
print("Tuple methods:")
print(f"len(colors) = {len(colors)}")
print(f"colors.index('green') = {colors.index('green')}")
print(f"colors.count('red') = {colors.count('red')}")
print()

# Dictionaries

# Creating dictionaries
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
grades = {"math": 95, "science": 87, "english": 92}

print("Creating dictionaries:")
print(f"empty_dict = {empty_dict}")
print(f"person = {person}")
print(f"grades = {grades}")
print()

# Dictionary operations
print("Dictionary operations:")
# Accessing values
print(f"person['name'] = {person['name']}")
print(f"grades['math'] = {grades['math']}")

# Using get() method (safer)
print(f"person.get('age') = {person.get('age')}")
print(f"person.get('salary', 'Not found') = {person.get('salary', 'Not found')}")

# Modifying dictionaries
person["email"] = "alice@example.com"  # Add new key-value pair
print(f"After adding email: {person}")

person["age"] = 31  # Update value
print(f"After updating age: {person}")

del person["city"]  # Remove key-value pair
print(f"After deleting city: {person}")

# Dictionary methods
print("Dictionary methods:")
print(f"person.keys() = {list(person.keys())}")
print(f"person.values() = {list(person.values())}")
print(f"person.items() = {list(person.items())}")
print(f"len(person) = {len(person)}")
print(f"'name' in person = {'name' in person}")
print()

# Iterating over collections

print("Iterating over collections:")

# Lists
print("Iterating over list:")
for fruit in fruits:
    print(f"  {fruit}")

# Tuples
print("Iterating over tuple:")
for color in colors:
    print(f"  {color}")

# Dictionaries
print("Iterating over dictionary:")
for key, value in grades.items():
    print(f"  {key}: {value}")

print()

# List comprehensions (advanced list creation)
print("List comprehensions:")
squares = [x**2 for x in range(1, 6)]
print(f"squares = {squares}")

even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"even_numbers = {even_numbers}")

# Nested data structures
print("Nested data structures:")
students = [
    {"name": "Alice", "grades": [85, 90, 88]},
    {"name": "Bob", "grades": [78, 82, 80]},
    {"name": "Charlie", "grades": [92, 95, 89]}
]

print("Students data:")
for student in students:
    avg_grade = sum(student["grades"]) / len(student["grades"])
    print(f"  {student['name']}: {student['grades']} (avg: {avg_grade:.1f})")

# Converting between types
print("Converting between types:")
# List to tuple
list_to_tuple = tuple([1, 2, 3])
print(f"tuple([1, 2, 3]) = {list_to_tuple}")

# Tuple to list
tuple_to_list = list((4, 5, 6))
print(f"list((4, 5, 6)) = {tuple_to_list}")

# Dict to list of keys/values
dict_keys = list(person.keys())
dict_values = list(person.values())
print(f"list(person.keys()) = {dict_keys}")
print(f"list(person.values()) = {dict_values}")

# Common use cases in data analysis
print("\nData analysis use cases:")

# Storing dataset columns
dataset = {
    "names": ["Alice", "Bob", "Charlie"],
    "ages": [25, 30, 35],
    "scores": [85, 90, 88]
}

print("Dataset structure:")
for key, value in dataset.items():
    print(f"  {key}: {value}")

# Calculating statistics
scores = dataset["scores"]
print(f"Average score: {sum(scores)/len(scores)}")
print(f"Highest score: {max(scores)}")

print("\nCollections demo completed!")
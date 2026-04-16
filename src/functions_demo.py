# Demo for Defining and Calling Python Functions

# Functions are reusable blocks of code that perform specific tasks.
# They help organize code, avoid repetition, and make programs more modular.
# Functions can take parameters and return values.
# Defining functions uses the 'def' keyword.

# Basic function definition and call
def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

print("Basic function:")
greet()
print()

# Function with parameters
def greet_person(name):
    """Greet a specific person by name."""
    print(f"Hello, {name}!")

print("Function with parameters:")
greet_person("Alice")
greet_person("Bob")
print()

# Function with return value
def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

print("Function with return value:")
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")
print()

# Function with multiple parameters and return
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

print("Function with multiple parameters:")
area = calculate_rectangle_area(10, 5)
print(f"Rectangle area: {area}")
print()

# Default parameters
def greet_with_time(name, time_of_day="morning"):
    """Greet someone with a time-specific message."""
    print(f"Good {time_of_day}, {name}!")

print("Function with default parameters:")
greet_with_time("Alice")
greet_with_time("Bob", "afternoon")
print()

# Keyword arguments
def describe_person(name, age, city):
    """Describe a person with their details."""
    print(f"{name} is {age} years old and lives in {city}.")

print("Function with keyword arguments:")
describe_person(name="Alice", age=30, city="New York")
describe_person(city="London", name="Bob", age=25)  # Order doesn't matter
print()

# Variable number of arguments (*args)
def sum_all(*numbers):
    """Sum any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print("Function with variable arguments:")
print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40: {sum_all(10, 20, 30, 40)}")
print()

# Keyword variable arguments (**kwargs)
def print_info(**info):
    """Print key-value information."""
    for key, value in info.items():
        print(f"{key}: {value}")

print("Function with keyword variable arguments:")
print_info(name="Alice", age=30, city="New York", occupation="Engineer")
print()

# Function that returns multiple values
def get_min_max(numbers):
    """Return the minimum and maximum values from a list."""
    return min(numbers), max(numbers)

print("Function returning multiple values:")
numbers = [5, 2, 8, 1, 9]
minimum, maximum = get_min_max(numbers)
print(f"Numbers: {numbers}")
print(f"Min: {minimum}, Max: {maximum}")
print()

# Recursive function
def factorial(n):
    """Calculate factorial recursively."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Recursive function:")
print(f"Factorial of 5: {factorial(5)}")
print()

# Lambda functions (anonymous functions)
print("Lambda functions:")
# Simple lambda
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda a, b: a + b
print(f"3 + 4 = {add(3, 4)}")

# Using lambda in sorting
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
students.sort(key=lambda student: student[1], reverse=True)
print(f"Students sorted by score: {students}")
print()

# Function documentation
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The average of the numbers.

    Raises:
        ValueError: If the list is empty.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)

print("Function with documentation:")
try:
    avg = calculate_average([10, 20, 30, 40])
    print(f"Average: {avg}")
except ValueError as e:
    print(f"Error: {e}")
print()

# Scope of variables
global_var = "I'm global"

def demonstrate_scope():
    local_var = "I'm local"
    print(f"Inside function: global_var = {global_var}")
    print(f"Inside function: local_var = {local_var}")

print("Variable scope:")
demonstrate_scope()
print(f"Outside function: global_var = {global_var}")
# print(local_var)  # This would cause an error
print()

# Practical examples for data analysis

# Function to clean data
def clean_text(text):
    """Clean text by removing extra spaces and converting to lowercase."""
    return text.strip().lower()

print("Data cleaning function:")
dirty_text = "  Hello World  "
cleaned = clean_text(dirty_text)
print(f"Original: '{dirty_text}'")
print(f"Cleaned: '{cleaned}'")
print()

# Function to calculate statistics
def calculate_stats(data):
    """Calculate basic statistics for a dataset."""
    if not data:
        return None

    stats = {
        'count': len(data),
        'mean': sum(data) / len(data),
        'min': min(data),
        'max': max(data)
    }
    return stats

print("Statistics function:")
dataset = [85, 92, 78, 96, 88, 91]
stats = calculate_stats(dataset)
if stats:
    for key, value in stats.items():
        print(f"{key}: {value}")
print()

# Function to filter data
def filter_above_threshold(data, threshold):
    """Filter values above a threshold."""
    return [x for x in data if x > threshold]

print("Data filtering function:")
scores = [75, 85, 95, 65, 80, 90]
filtered = filter_above_threshold(scores, 80)
print(f"Original scores: {scores}")
print(f"Scores above 80: {filtered}")
print()

# Function composition
def process_data(data):
    """Process data through multiple steps."""
    # Clean data
    cleaned = [x for x in data if isinstance(x, (int, float))]

    # Calculate stats
    if cleaned:
        stats = calculate_stats(cleaned)
        return stats
    return None

print("Function composition:")
mixed_data = [10, "invalid", 20, None, 30, 25.5]
result = process_data(mixed_data)
if result:
    print("Processed data stats:")
    for key, value in result.items():
        print(f"  {key}: {value}")
print()

# Best practices
print("Best practices for functions:")
print("1. Use descriptive function names")
print("2. Add docstrings to document purpose and parameters")
print("3. Keep functions focused on a single task")
print("4. Use meaningful parameter names")
print("5. Return values rather than printing inside functions")
print("6. Handle edge cases and errors")
print("7. Use default parameters when appropriate")

print("\nFunctions demo completed!")
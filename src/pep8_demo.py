# Demo for Writing Readable Variable Names and Comments (PEP8 Basics)

# PEP8 is Python's style guide that makes code more readable and consistent.
# Good variable names and comments make code self-documenting.
# Following PEP8 conventions helps collaboration and maintenance.
# This demo shows good practices vs bad practices.

# Bad examples (don't do this!)
# x = 25  # What does x represent?
# y = "Alice"  # Unclear variable name
# a = [1, 2, 3]  # Not descriptive
# def f(x, y):  # What does f do?
#     return x + y  # No comment explaining logic

# Good examples (follow these!)

# Descriptive variable names
user_age = 25
user_name = "Alice"
test_scores = [85, 92, 78, 96]

print("Good variable naming:")
print(f"User {user_name} is {user_age} years old.")
print(f"Test scores: {test_scores}")
print()

# Function with clear name and documentation
def calculate_average_score(scores):
    """
    Calculate the average of a list of scores.

    Args:
        scores (list): List of numeric scores

    Returns:
        float: Average score
    """
    if not scores:
        return 0.0

    total = sum(scores)
    average = total / len(scores)
    return average

print("Well-documented function:")
average = calculate_average_score(test_scores)
print(f"Average score: {average:.2f}")
print()

# Constants in UPPERCASE
MAX_SCORE = 100
MIN_PASSING_SCORE = 60
PI = 3.14159

print("Constants:")
print(f"Maximum score: {MAX_SCORE}")
print(f"Minimum passing score: {MIN_PASSING_SCORE}")
print()

# Private variables with underscore prefix
class Student:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self._age = age   # Protected attribute (convention)
        self.__id = None  # Private attribute (name mangling)

# Clear loop variables
def process_student_data(students):
    """Process a list of student dictionaries."""
    total_age = 0
    student_count = 0

    for student in students:  # Clear loop variable
        current_age = student.get('age', 0)
        total_age += current_age
        student_count += 1

    if student_count > 0:
        average_age = total_age / student_count
        return average_age
    return 0

print("Clear loop variables:")
student_list = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 22},
    {'name': 'Charlie', 'age': 21}
]
avg_age = process_student_data(student_list)
print(f"Average student age: {avg_age:.1f}")
print()

# Good commenting practices

# Single-line comments
temperature = 25  # Temperature in Celsius

# Multi-line comments
"""
This function validates user input.
It checks for:
- Non-empty strings
- Reasonable length
- Valid characters
"""
def validate_input(user_input):
    if not user_input:  # Empty check
        return False, "Input cannot be empty"

    if len(user_input) > 100:  # Length check
        return False, "Input too long"

    # Check for valid characters (simplified)
    valid_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?')
    if not all(char in valid_chars for char in user_input):
        return False, "Invalid characters"

    return True, "Valid input"

print("Input validation with comments:")
test_inputs = ["", "Valid input!", "Input with invalid chars @#$"]
for test_input in test_inputs:
    is_valid, message = validate_input(test_input)
    print(f"'{test_input}': {message}")
print()

# Block comments for complex logic
def calculate_grade(score):
    """
    Calculate letter grade based on score.

    Grading scale:
    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    F: 0-59
    """
    # Input validation
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return "Invalid score"

    # Determine grade based on score ranges
    if score >= 90:
        return "A"
    elif score >= 80:  # 80-89 range
        return "B"
    elif score >= 70:  # 70-79 range
        return "C"
    elif score >= 60:  # 60-69 range
        return "D"
    else:  # 0-59 range
        return "F"

print("Grade calculation with detailed comments:")
scores_to_test = [95, 85, 75, 65, 55, 105, -5]
for score in scores_to_test:
    grade = calculate_grade(score)
    print(f"Score {score}: Grade {grade}")
print()

# PEP8 spacing and formatting
# Good: spaces around operators
result = 2 + 3 * 4  # Clear precedence

# Good: spaces after commas
numbers = [1, 2, 3, 4, 5]

# Good: consistent indentation
def example_function(param1, param2):
    """Example function with proper formatting."""
    if param1 > param2:
        return param1
    else:
        return param2

# Bad examples (commented out to avoid syntax errors):
# result=2+3*4  # No spaces
# numbers=[1,2,3,4,5]  # No spaces after commas
# def bad_function(param1,param2):  # No spaces after commas

print("Proper formatting example:")
larger = example_function(10, 5)
print(f"Larger of 10 and 5: {larger}")
print()

# Naming conventions
# snake_case for variables and functions
user_name = "Alice"
def calculate_total():
    pass

# CamelCase for classes
class DataProcessor:
    def __init__(self):
        self.data = []

    def process_data(self, input_data):
        """Process input data."""
        self.data = input_data
        # Processing logic here
        return self.data

print("Class with proper naming:")
processor = DataProcessor()
processed = processor.process_data([1, 2, 3, 4])
print(f"Processed data: {processed}")
print()

# Meaningful error messages and logging
def divide_numbers(dividend, divisor):
    """Divide two numbers with proper error handling."""
    try:
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        result = dividend / divisor
        return result
    except TypeError:
        raise TypeError("Both dividend and divisor must be numbers")

print("Error handling with clear messages:")
try:
    result = divide_numbers(10, 2)
    print(f"10 ÷ 2 = {result}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

try:
    result = divide_numbers(10, 0)
    print(f"Result: {result}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
print()

# Code organization with comments
# ====================
# DATA PROCESSING SECTION
# ====================

def load_data(file_path):
    """Load data from file."""
    # Implementation would go here
    return []

def clean_data(raw_data):
    """Clean and validate data."""
    # Remove invalid entries
    # Handle missing values
    return raw_data

def analyze_data(cleaned_data):
    """Perform analysis on cleaned data."""
    # Calculate statistics
    # Generate insights
    return {}

# ====================
# MAIN EXECUTION
# ====================

def main():
    """Main execution function."""
    # Load data
    data = load_data("data.csv")

    # Clean data
    cleaned = clean_data(data)

    # Analyze data
    results = analyze_data(cleaned)

    return results

print("Code organization example:")
print("Main function defined with clear sections")
print()

# Best practices summary
print("PEP8 and readability best practices:")
print("1. Use descriptive variable names (user_age, not x)")
print("2. Write docstrings for functions and classes")
print("3. Use UPPERCASE for constants")
print("4. Add comments for complex logic")
print("5. Use snake_case for variables/functions")
print("6. Use spaces around operators and after commas")
print("7. Keep lines under 79 characters")
print("8. Use blank lines to separate logical sections")
print("9. Handle errors with clear messages")
print("10. Organize code with comments and consistent structure")

# Practical example: data analysis with good practices
def analyze_sales_data(sales_records):
    """
    Analyze sales data and return summary statistics.

    Args:
        sales_records (list): List of sales amounts

    Returns:
        dict: Summary statistics
    """
    if not sales_records:
        return {"error": "No sales records provided"}

    # Calculate basic statistics
    total_sales = sum(sales_records)
    number_of_sales = len(sales_records)
    average_sale = total_sales / number_of_sales
    max_sale = max(sales_records)
    min_sale = min(sales_records)

    # Create summary dictionary
    sales_summary = {
        "total_sales": total_sales,
        "number_of_sales": number_of_sales,
        "average_sale": round(average_sale, 2),
        "highest_sale": max_sale,
        "lowest_sale": min_sale
    }

    return sales_summary

print("\nData analysis with good practices:")
monthly_sales = [1200, 1500, 1100, 1800, 1400, 1600]
summary = analyze_sales_data(monthly_sales)
for key, value in summary.items():
    print(f"{key}: {value}")

print("\nPEP8 basics demo completed!")
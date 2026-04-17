# Demo for Passing Data into Functions and Returning Results

# Functions can receive data through parameters and send results back using return.
# Parameters allow functions to work with different inputs.
# Return statements send computed values back to the caller.
# Understanding parameter passing and return values is key to modular programming.

# Basic parameter passing
def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"

print("Basic parameter passing:")
message = greet("Alice")
print(message)
print()

# Multiple parameters
def calculate_total(price, quantity, tax_rate=0.08):
    """Calculate total cost including tax."""
    subtotal = price * quantity
    tax = subtotal * tax_rate
    total = subtotal + tax
    return total

print("Multiple parameters:")
total_cost = calculate_total(10.99, 3)
print(f"Total cost: ${total_cost:.2f}")

total_with_tax = calculate_total(10.99, 3, 0.10)
print(f"Total with 10% tax: ${total_with_tax:.2f}")
print()

# Returning multiple values
def analyze_numbers(numbers):
    """Analyze a list of numbers and return multiple statistics."""
    if not numbers:
        return 0, 0, 0, 0

    total = sum(numbers)
    average = total / len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)

    return total, average, minimum, maximum

print("Returning multiple values:")
data = [10, 20, 30, 40, 50]
total, avg, min_val, max_val = analyze_numbers(data)
print(f"Data: {data}")
print(f"Total: {total}, Average: {avg:.1f}, Min: {min_val}, Max: {max_val}")
print()

# Using *args for variable number of arguments
def sum_all(*values):
    """Sum any number of numeric values."""
    total = 0
    for value in values:
        if isinstance(value, (int, float)):
            total += value
    return total

print("Variable arguments (*args):")
print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40, 50: {sum_all(10, 20, 30, 40, 50)}")
print()

# Using **kwargs for keyword arguments
def create_profile(**details):
    """Create a profile dictionary from keyword arguments."""
    profile = {}
    for key, value in details.items():
        profile[key] = value
    return profile

print("Keyword arguments (**kwargs):")
profile1 = create_profile(name="Alice", age=30, city="New York")
print(f"Profile 1: {profile1}")

profile2 = create_profile(name="Bob", occupation="Engineer", hobbies=["reading", "coding"])
print(f"Profile 2: {profile2}")
print()

# Combining *args and **kwargs
def flexible_function(*args, **kwargs):
    """Demonstrate both *args and **kwargs."""
    print("Positional arguments:")
    for i, arg in enumerate(args):
        print(f"  {i}: {arg}")

    print("Keyword arguments:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

    return len(args), len(kwargs)

print("Combining *args and **kwargs:")
pos_count, kw_count = flexible_function(1, 2, 3, name="Alice", age=30)
print(f"Positional args count: {pos_count}, Keyword args count: {kw_count}")
print()

# Parameter passing by reference vs value
def modify_list(my_list):
    """Modify a list (mutable object)."""
    my_list.append(100)
    return my_list

def modify_number(my_number):
    """Try to modify a number (immutable object)."""
    my_number = my_number + 10
    return my_number

print("Parameter passing behavior:")
original_list = [1, 2, 3]
print(f"Original list: {original_list}")
modified_list = modify_list(original_list)
print(f"After function call: {original_list}")  # List is modified!
print(f"Returned list: {modified_list}")
print()

original_number = 5
print(f"Original number: {original_number}")
modified_number = modify_number(original_number)
print(f"After function call: {original_number}")  # Number unchanged
print(f"Returned number: {modified_number}")
print()

# Default parameter values
def configure_system(host="localhost", port=8080, debug=False):
    """Configure system with default values."""
    config = {
        "host": host,
        "port": port,
        "debug": debug
    }
    return config

print("Default parameter values:")
config1 = configure_system()
print(f"Default config: {config1}")

config2 = configure_system("example.com", 9000, True)
print(f"Custom config: {config2}")
print()

# Returning None vs returning values
def print_message(message):
    """Print a message and return None."""
    print(f"Message: {message}")

def get_message(message):
    """Return a message without printing."""
    return f"Message: {message}"

print("Return None vs return values:")
result1 = print_message("Hello")
print(f"print_message returned: {result1}")

result2 = get_message("Hello")
print(f"get_message returned: {result2}")
print()

# Early returns
def find_first_even(numbers):
    """Find the first even number in a list."""
    for num in numbers:
        if num % 2 == 0:
            return num  # Early return
    return None  # If no even number found

print("Early returns:")
numbers_list = [1, 3, 5, 6, 7, 9]
first_even = find_first_even(numbers_list)
print(f"First even in {numbers_list}: {first_even}")

no_even = find_first_even([1, 3, 5])
print(f"First even in [1, 3, 5]: {no_even}")
print()

# Data processing functions
def clean_data(data, remove_negatives=True, fill_missing=None):
    """Clean a list of data."""
    cleaned = []

    for item in data:
        if item is None and fill_missing is not None:
            cleaned.append(fill_missing)
        elif remove_negatives and isinstance(item, (int, float)) and item < 0:
            continue  # Skip negative numbers
        else:
            cleaned.append(item)

    return cleaned

print("Data processing function:")
raw_data = [10, -5, 20, None, 30, -2, 40]
cleaned_data = clean_data(raw_data)
print(f"Raw data: {raw_data}")
print(f"Cleaned data: {cleaned_data}")

# With different options
cleaned_keep_negatives = clean_data(raw_data, remove_negatives=False)
print(f"Cleaned (keep negatives): {cleaned_keep_negatives}")

cleaned_fill_missing = clean_data(raw_data, fill_missing=0)
print(f"Cleaned (fill missing): {cleaned_fill_missing}")
print()

# Function that returns a function
def create_multiplier(factor):
    """Return a function that multiplies by a factor."""
    def multiplier(number):
        return number * factor
    return multiplier

print("Function returning a function:")
double = create_multiplier(2)
triple = create_multiplier(3)

print(f"Double 5: {double(5)}")
print(f"Triple 5: {triple(5)}")
print()

# Error handling in functions
def safe_divide(a, b):
    """Safely divide two numbers."""
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid types"

print("Error handling in functions:")
print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'a' = {safe_divide(10, 'a')}")
print()

# Best practices for parameters and return
print("Best practices:")
print("1. Use descriptive parameter names")
print("2. Provide default values for optional parameters")
print("3. Document parameters and return values with docstrings")
print("4. Return meaningful values, not just print")
print("5. Handle edge cases and errors gracefully")
print("6. Use *args and **kwargs for flexible interfaces")
print("7. Keep functions focused on single responsibilities")

# Practical data analysis example
def process_dataset(data, operation="mean", threshold=None):
    """
    Process a dataset with various operations.

    Args:
        data: List of numeric values
        operation: "mean", "sum", "count", or "filter"
        threshold: Threshold for filtering (if operation is "filter")

    Returns:
        Processed result
    """
    if not data:
        return None

    if operation == "mean":
        return sum(data) / len(data)
    elif operation == "sum":
        return sum(data)
    elif operation == "count":
        return len(data)
    elif operation == "filter" and threshold is not None:
        return [x for x in data if x > threshold]
    else:
        return "Invalid operation"

print("\nData analysis example:")
dataset = [10, 20, 30, 40, 50]
print(f"Dataset: {dataset}")
print(f"Mean: {process_dataset(dataset, 'mean')}")
print(f"Sum: {process_dataset(dataset, 'sum')}")
print(f"Count: {process_dataset(dataset, 'count')}")
print(f"Filter > 25: {process_dataset(dataset, 'filter', 25)}")

print("\nFunction parameters and return demo completed!")
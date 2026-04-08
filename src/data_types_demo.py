# Demo for Understanding Python Numeric and String Data Types

# Python has several built-in data types for handling different kinds of data.
# Numeric types include integers and floating-point numbers.
# Strings are used for text data.
# Understanding data types is crucial for writing correct and efficient code.

# Numeric Data Types

# Integers (int): whole numbers, positive or negative
age = 25
year = 2023
negative_number = -10

print("Integer examples:")
print(f"age = {age}, type: {type(age)}")
print(f"year = {year}, type: {type(year)}")
print(f"negative_number = {negative_number}, type: {type(negative_number)}")
print()

# Floating-point numbers (float): numbers with decimal points
height = 5.9
temperature = 98.6
pi = 3.14159

print("Float examples:")
print(f"height = {height}, type: {type(height)}")
print(f"temperature = {temperature}, type: {type(temperature)}")
print(f"pi = {pi}, type: {type(pi)}")
print()

# Basic arithmetic operations with numeric types
a = 10
b = 3.5

print("Arithmetic operations:")
print(f"a + b = {a + b}, type: {type(a + b)}")  # Addition
print(f"a - b = {a - b}, type: {type(a - b)}")  # Subtraction
print(f"a * b = {a * b}, type: {type(a * b)}")  # Multiplication
print(f"a / b = {a / b}, type: {type(a / b)}")  # Division (always float)
print(f"a // b = {a // b}, type: {type(a // b)}")  # Floor division
print(f"a % b = {a % b}, type: {type(a % b)}")  # Modulo
print(f"a ** b = {a ** b}, type: {type(a ** b)}")  # Exponentiation
print()

# String Data Types

# Strings (str): sequences of characters
name = "Alice"
message = "Hello, World!"
empty_string = ""

print("String examples:")
print(f"name = '{name}', type: {type(name)}")
print(f"message = '{message}', type: {type(message)}")
print(f"empty_string = '{empty_string}', type: {type(empty_string)}")
print()

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation

print("String operations:")
print(f"first_name + ' ' + last_name = '{full_name}'")
print(f"len(full_name) = {len(full_name)}")  # Length
print(f"full_name.upper() = '{full_name.upper()}'")  # Uppercase
print(f"full_name.lower() = '{full_name.lower()}'")  # Lowercase
print(f"full_name.title() = '{full_name.title()}'")  # Title case
print()

# String indexing and slicing
text = "Python"
print("String indexing and slicing:")
print(f"text = '{text}'")
print(f"text[0] = '{text[0]}'")  # First character
print(f"text[-1] = '{text[-1]}'")  # Last character
print(f"text[1:4] = '{text[1:4]}'")  # Slice from index 1 to 3
print(f"text[:3] = '{text[:3]}'")  # First 3 characters
print(f"text[2:] = '{text[2:]}'")  # From index 2 to end
print()

# Type conversion
print("Type conversion:")
# String to int/float
num_str = "42"
num_int = int(num_str)
num_float = float(num_str)

print(f"int('{num_str}') = {num_int}, type: {type(num_int)}")
print(f"float('{num_str}') = {num_float}, type: {type(num_float)}")

# Int/float to string
number = 123
str_number = str(number)
print(f"str({number}) = '{str_number}', type: {type(str_number)}")

# Float to int (truncates)
float_num = 3.9
int_from_float = int(float_num)
print(f"int({float_num}) = {int_from_float}, type: {type(int_from_float)}")
print()

# More numeric examples
print("More numeric examples:")
# Large numbers
big_number = 1000000
scientific = 1.23e6  # Scientific notation

print(f"big_number = {big_number}")
print(f"scientific = {scientific}")

# Boolean as numeric (True = 1, False = 0)
is_active = True
is_inactive = False

print(f"True + 1 = {is_active + 1}")
print(f"False * 5 = {is_inactive * 5}")
print()

# String formatting
print("String formatting:")
price = 19.99
quantity = 3

# Old style
old_style = "Price: $%0.2f, Quantity: %d" % (price, quantity)
print(f"Old style: '{old_style}'")

# New style
new_style = "Price: ${:.2f}, Quantity: {}".format(price, quantity)
print(f"New style: '{new_style}'")

# f-strings (Python 3.6+)
f_string = f"Price: ${price:.2f}, Quantity: {quantity}"
print(f"f-string: '{f_string}'")
print()

# String methods
sample_text = "  Hello, Python World!  "
print("String methods:")
print(f"Original: '{sample_text}'")
print(f"Stripped: '{sample_text.strip()}'")
print(f"Replaced: '{sample_text.replace('Python', 'Data Science')}'")
print(f"Split: {sample_text.split()}")
print(f"Joined: {'-'.join(['Hello', 'World'])}")
print()

# Checking data types
print("Type checking:")
variables = [age, height, name, is_active]

for var in variables:
    print(f"{var} is {type(var).__name__}")

print()

# Common mistakes and tips
print("Common tips:")
print("1. Division always returns float: 5/2 = 2.5")
print("2. Use // for integer division: 5//2 = 2")
print("3. Strings are immutable: you can't change a character in place")
print("4. Use type() to check variable types")
print("5. Be careful with type conversion: int('3.14') will fail")

# Examples with data analysis context
print("\nData analysis examples:")

# Numeric data
sales = 150.50
units_sold = 25
product_name = "Widget"

print(f"Product: {product_name}")
print(f"Units sold: {units_sold}")
print(f"Sales amount: ${sales}")
print(f"Average price per unit: ${sales / units_sold:.2f}")

# String processing
customer_feedback = "Great product! Highly recommended."
word_count = len(customer_feedback.split())
print(f"Feedback: '{customer_feedback}'")
print(f"Word count: {word_count}")

print("\nData types demo completed!")
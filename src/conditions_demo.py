# Demo for Writing Conditional Statements (if, elif, else)

# Conditional statements allow your program to make decisions based on conditions.
# The if statement executes code only if a condition is true.
# elif (else if) allows checking multiple conditions.
# else executes when none of the conditions are true.
# This is fundamental for controlling program flow.

# Basic if statement
print("Basic if statement:")

age = 18
if age >= 18:
    print("You are an adult.")
print("This always prints.")
print()

# if-else statement
print("if-else statement:")

temperature = 25
if temperature > 30:
    print("It's hot outside.")
else:
    print("It's not too hot.")
print()

# if-elif-else statement
print("if-elif-else statement:")

score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")
print()

# Multiple conditions with logical operators
print("Multiple conditions:")

# and operator
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive.")
else:
    print("You cannot drive.")

# or operator
is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("You can relax.")
else:
    print("Time to work.")

# not operator
is_raining = False
if not is_raining:
    print("No need for an umbrella.")
else:
    print("Take an umbrella.")
print()

# Nested if statements
print("Nested if statements:")

age = 20
has_job = True

if age >= 18:
    if has_job:
        print("You are an employed adult.")
    else:
        print("You are an unemployed adult.")
else:
    print("You are a minor.")
print()

# Conditional expressions (ternary operator)
print("Conditional expressions:")

# Traditional if-else
number = 5
if number % 2 == 0:
    result = "even"
else:
    result = "odd"
print(f"{number} is {result}")

# Conditional expression
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result} (using conditional expression)")
print()

# Comparing values
print("Comparing values:")

a = 10
b = 20

if a < b:
    print(f"{a} is less than {b}")
elif a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is equal to {b}")

# String comparison
name1 = "Alice"
name2 = "Bob"
if name1 < name2:
    print(f"{name1} comes before {name2} alphabetically")
else:
    print(f"{name1} comes after or is equal to {name2}")
print()

# Checking membership
print("Checking membership:")

fruits = ["apple", "banana", "cherry"]
favorite = "banana"

if favorite in fruits:
    print(f"{favorite} is in the list of fruits.")
else:
    print(f"{favorite} is not in the list of fruits.")

# Checking if empty
shopping_list = []
if not shopping_list:
    print("Shopping list is empty.")
else:
    print("Shopping list has items.")
print()

# Real-world examples
print("Real-world examples:")

# Temperature advice
temp = 15
if temp < 0:
    advice = "Wear a heavy coat!"
elif temp < 10:
    advice = "Wear a jacket."
elif temp < 20:
    advice = "Wear a light sweater."
else:
    advice = "Wear light clothing."
print(f"Temperature: {temp}°C - {advice}")

# User authentication
username = "admin"
password = "secret"

if username == "admin" and password == "secret":
    print("Login successful!")
else:
    print("Login failed.")

# Age categories
person_age = 65
if person_age < 13:
    category = "child"
elif person_age < 20:
    category = "teenager"
elif person_age < 65:
    category = "adult"
else:
    category = "senior"
print(f"Age {person_age} - Category: {category}")
print()

# Data validation
print("Data validation examples:")

# Check if number is positive
num = -5
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")

# Validate email (simple check)
email = "user@example.com"
if "@" in email and "." in email:
    print("Email format looks valid.")
else:
    print("Email format is invalid.")
print()

# Complex conditions
print("Complex conditions:")

# Grade calculator with multiple criteria
attendance = 85
homework_avg = 90
exam_score = 75

if attendance >= 80 and homework_avg >= 70 and exam_score >= 60:
    if exam_score >= 90:
        final_grade = "A"
    elif exam_score >= 80:
        final_grade = "B"
    elif exam_score >= 70:
        final_grade = "C"
    else:
        final_grade = "D"
    print(f"Final grade: {final_grade}")
else:
    print("Did not meet minimum requirements for grading.")
print()

# Using conditions with loops (preview)
print("Conditions with loops:")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Even numbers from {numbers}: {even_numbers}")
print()

# Best practices
print("Best practices for conditional statements:")
print("1. Use clear, descriptive variable names")
print("2. Keep conditions simple and readable")
print("3. Use parentheses for complex conditions")
print("4. Consider using elif for mutually exclusive conditions")
print("5. Test edge cases (boundaries)")
print("6. Use comments to explain complex logic")

print("\nConditional statements demo completed!")
# Demo for Performing Basic Mathematical Operations on NumPy Arrays

# NumPy provides efficient mathematical operations on arrays.
# Operations can be performed element-wise or on entire arrays.
# Broadcasting allows operations between arrays of different shapes.
# Mathematical functions work on both scalars and arrays.

import numpy as np

# Basic arithmetic operations
print("Basic arithmetic operations:")

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a = {a}")
print(f"b = {b}")
print()

# Element-wise addition
print("Addition:")
print(f"a + b = {a + b}")
print(f"np.add(a, b) = {np.add(a, b)}")
print()

# Element-wise subtraction
print("Subtraction:")
print(f"a - b = {a - b}")
print(f"np.subtract(a, b) = {np.subtract(a, b)}")
print()

# Element-wise multiplication
print("Multiplication:")
print(f"a * b = {a * b}")
print(f"np.multiply(a, b) = {np.multiply(a, b)}")
print()

# Element-wise division
print("Division:")
print(f"b / a = {b / a}")
print(f"np.divide(b, a) = {np.divide(b, a)}")
print()

# Power operations
print("Power operations:")
print(f"a ** 2 = {a ** 2}")
print(f"np.power(a, 2) = {np.power(a, 2)}")
print(f"np.power(a, b) = {np.power(a, b)}")
print()

# Operations with scalars
print("Operations with scalars:")
scalar = 10
print(f"a + {scalar} = {a + scalar}")
print(f"a * {scalar} = {a * scalar}")
print(f"a ** {scalar} = {a ** 10}")
print()

# Mathematical functions
print("Mathematical functions:")

angles = np.array([0, np.pi/4, np.pi/2, np.pi])
print(f"angles = {angles}")

print(f"sin(angles) = {np.sin(angles)}")
print(f"cos(angles) = {np.cos(angles)}")
print(f"tan(angles) = {np.tan(angles)}")
print()

# Exponential and logarithmic functions
values = np.array([1, 2, 3, 4])
print(f"values = {values}")

print(f"exp(values) = {np.exp(values)}")
print(f"log(values) = {np.log(values)}")
print(f"sqrt(values) = {np.sqrt(values)}")
print()

# Statistical operations
print("Statistical operations:")

data = np.array([10, 20, 30, 40, 50])
print(f"data = {data}")

print(f"sum = {np.sum(data)}")
print(f"mean = {np.mean(data)}")
print(f"median = {np.median(data)}")
print(f"std = {np.std(data)}")
print(f"var = {np.var(data)}")
print(f"min = {np.min(data)}")
print(f"max = {np.max(data)}")
print()

# Operations on multi-dimensional arrays
print("Multi-dimensional array operations:")

matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

print(f"matrix_a =\n{matrix_a}")
print(f"matrix_b =\n{matrix_b}")
print()

print("Matrix addition:")
print(f"matrix_a + matrix_b =\n{matrix_a + matrix_b}")
print()

print("Matrix multiplication (element-wise):")
print(f"matrix_a * matrix_b =\n{matrix_a * matrix_b}")
print()

print("Matrix multiplication (dot product):")
print(f"np.dot(matrix_a, matrix_b) =\n{np.dot(matrix_a, matrix_b)}")
print(f"matrix_a @ matrix_b =\n{matrix_a @ matrix_b}")
print()

# Broadcasting
print("Broadcasting operations:")

# Array and scalar
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
scalar_val = 10

print(f"array_2d =\n{array_2d}")
print(f"scalar_val = {scalar_val}")
print(f"array_2d + scalar_val =\n{array_2d + scalar_val}")
print()

# Broadcasting with different shapes
array_1d = np.array([1, 2, 3])
array_2d_small = np.array([[10], [20]])

print(f"array_1d = {array_1d}")
print(f"array_2d_small =\n{array_2d_small}")
print(f"array_2d_small + array_1d =\n{array_2d_small + array_1d}")
print()

# Aggregation operations
print("Aggregation operations:")

large_array = np.arange(12).reshape(3, 4)
print(f"large_array =\n{large_array}")
print()

print("Sum along different axes:")
print(f"sum all = {np.sum(large_array)}")
print(f"sum rows (axis=0) = {np.sum(large_array, axis=0)}")
print(f"sum columns (axis=1) = {np.sum(large_array, axis=1)}")
print()

print("Mean along different axes:")
print(f"mean all = {np.mean(large_array)}")
print(f"mean rows = {np.mean(large_array, axis=0)}")
print(f"mean columns = {np.mean(large_array, axis=1)}")
print()

# Comparison operations
print("Comparison operations:")

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])

print(f"x = {x}")
print(f"y = {y}")
print()

print("Comparisons:")
print(f"x > y = {x > y}")
print(f"x < y = {x < y}")
print(f"x == y = {x == y}")
print(f"x >= 3 = {x >= 3}")
print()

# Boolean operations on arrays
comparison_result = x > 3
print(f"x > 3 = {comparison_result}")
print(f"any(x > 3) = {np.any(comparison_result)}")
print(f"all(x > 3) = {np.all(comparison_result)}")
print(f"sum(x > 3) = {np.sum(comparison_result)}")  # Count of True values
print()

# Trigonometric and hyperbolic functions
print("Trigonometric functions:")

angles_deg = np.array([0, 30, 45, 60, 90])
angles_rad = np.radians(angles_deg)

print(f"angles (degrees) = {angles_deg}")
print(f"sin(angles) = {np.sin(angles_rad)}")
print(f"cos(angles) = {np.cos(angles_rad)}")
print(f"tan(angles) = {np.tan(angles_rad)}")
print()

# Rounding functions
print("Rounding functions:")

float_array = np.array([1.234, 2.567, 3.891, 4.123])
print(f"float_array = {float_array}")

print(f"round (to nearest) = {np.round(float_array)}")
print(f"floor = {np.floor(float_array)}")
print(f"ceil = {np.ceil(float_array)}")
print(f"trunc = {np.trunc(float_array)}")
print()

# Absolute values and signs
print("Absolute values and signs:")

mixed_numbers = np.array([-3, -2, -1, 0, 1, 2, 3])
print(f"mixed_numbers = {mixed_numbers}")

print(f"abs = {np.abs(mixed_numbers)}")
print(f"sign = {np.sign(mixed_numbers)}")
print()

# Data analysis examples
print("Data analysis examples:")

# Temperature data analysis
temperatures = np.array([20.5, 22.1, 19.8, 21.3, 23.0, 18.9, 24.2])
print(f"Temperature readings: {temperatures}")

# Basic statistics
print(f"Average temperature: {np.mean(temperatures):.1f}°C")
print(f"Temperature range: {np.max(temperatures) - np.min(temperatures):.1f}°C")
print(f"Days above 22°C: {np.sum(temperatures > 22)}")

# Normalize temperatures (subtract mean, divide by std)
normalized = (temperatures - np.mean(temperatures)) / np.std(temperatures)
print(f"Normalized temperatures: {normalized}")
print()

# Sales data analysis
monthly_sales = np.array([1200, 1500, 1100, 1800, 1400, 1600])
quarterly_goals = np.array([1300, 1400, 1500, 1600])

print(f"Monthly sales: {monthly_sales}")
print(f"Quarterly goals: {quarterly_goals}")

# Calculate performance vs goals
performance = monthly_sales - quarterly_goals[:len(monthly_sales)]
print(f"Performance vs goals: {performance}")

# Check which months met goals
met_goals = monthly_sales >= quarterly_goals[:len(monthly_sales)]
print(f"Met goals: {met_goals}")
print(f"Months meeting goals: {np.sum(met_goals)}")
print()

# Matrix operations for data transformation
print("Matrix operations for data transformation:")

# Sample dataset (features x samples)
dataset = np.array([[1, 2, 3, 4, 5],
                    [10, 20, 30, 40, 50],
                    [100, 200, 300, 400, 500]])

print(f"Dataset (3 features x 5 samples):\n{dataset}")

# Transpose
print(f"Transposed:\n{dataset.T}")

# Normalize each feature (subtract mean, divide by std)
feature_means = np.mean(dataset, axis=1, keepdims=True)
feature_stds = np.std(dataset, axis=1, keepdims=True)
normalized_dataset = (dataset - feature_means) / feature_stds

print(f"Normalized dataset:\n{normalized_dataset}")
print()

# Performance comparison with Python lists
print("Performance comparison:")

import time

# Large arrays
size = 1000000
np_array = np.random.rand(size)
py_list = list(np_array)

# Sum operation
start = time.time()
np_sum = np.sum(np_array)
np_time = time.time() - start

start = time.time()
py_sum = sum(py_list)
py_time = time.time() - start

print(f"NumPy sum time: {np_time:.4f} seconds")
print(f"Python list sum time: {py_time:.4f} seconds")
print(f"NumPy is {py_time/np_time:.1f}x faster")
print()

# Best practices
print("Best practices for NumPy operations:")
print("1. Use vectorized operations instead of loops")
print("2. Understand broadcasting rules")
print("3. Use appropriate data types to save memory")
print("4. Be aware of axis parameter in aggregation functions")
print("5. Use np.dot() or @ for matrix multiplication")
print("6. Check array shapes before operations")
print("7. Use np.allclose() for floating-point comparisons")
print("8. Leverage NumPy's mathematical functions over math module")

print("\nNumPy operations demo completed!")
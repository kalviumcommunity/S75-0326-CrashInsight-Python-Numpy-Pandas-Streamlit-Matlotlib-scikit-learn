# Demo for Creating NumPy Arrays from Python Lists

# NumPy is a fundamental package for scientific computing in Python.
# NumPy arrays are more efficient than Python lists for numerical operations.
# Arrays can be created from lists and provide powerful mathematical capabilities.
# Understanding array creation is the first step to using NumPy effectively.

import numpy as np

# Creating arrays from lists

# 1D array from a list
print("Creating 1D arrays from lists:")
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array(python_list)

print(f"Python list: {python_list}")
print(f"NumPy array: {numpy_array}")
print(f"Type: {type(numpy_array)}")
print(f"Shape: {numpy_array.shape}")
print(f"Data type: {numpy_array.dtype}")
print()

# 2D array from nested lists
print("Creating 2D arrays from nested lists:")
matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_array = np.array(matrix_list)

print(f"Nested list: {matrix_list}")
print(f"NumPy 2D array:\n{matrix_array}")
print(f"Shape: {matrix_array.shape}")
print(f"Dimensions: {matrix_array.ndim}")
print()

# Arrays with different data types
print("Arrays with different data types:")

# Integer array
int_list = [1, 2, 3, 4, 5]
int_array = np.array(int_list)
print(f"Integer array: {int_array}, dtype: {int_array.dtype}")

# Float array
float_list = [1.1, 2.2, 3.3, 4.4, 5.5]
float_array = np.array(float_list)
print(f"Float array: {float_array}, dtype: {float_array.dtype}")

# Mixed types (NumPy will find a common type)
mixed_list = [1, 2.5, 3, 4.0]
mixed_array = np.array(mixed_list)
print(f"Mixed array: {mixed_array}, dtype: {mixed_array.dtype}")

# Explicitly specify data type
explicit_float = np.array([1, 2, 3, 4], dtype=float)
print(f"Explicit float: {explicit_float}, dtype: {explicit_float.dtype}")
print()

# Special array creation functions
print("Special array creation functions:")

# Array of zeros
zeros_array = np.zeros(5)
print(f"Zeros array: {zeros_array}")

# Array of ones
ones_array = np.ones(5)
print(f"Ones array: {ones_array}")

# Array with a range of values
range_array = np.arange(10)
print(f"Range array: {range_array}")

# Array with evenly spaced values
linspace_array = np.linspace(0, 1, 5)
print(f"Linspace array: {linspace_array}")

# Identity matrix
identity_matrix = np.eye(3)
print(f"Identity matrix:\n{identity_matrix}")
print()

# Creating arrays from different sources
print("Creating arrays from different sources:")

# From tuple
tuple_data = (1, 2, 3, 4, 5)
tuple_array = np.array(tuple_data)
print(f"From tuple: {tuple_array}")

# From range object
range_obj = range(5)
range_array = np.array(range_obj)
print(f"From range: {range_array}")

# From list comprehension
comprehension_list = [x**2 for x in range(5)]
comprehension_array = np.array(comprehension_list)
print(f"From comprehension: {comprehension_array}")
print()

# Array properties and methods
print("Array properties and methods:")
sample_array = np.array([10, 20, 30, 40, 50])

print(f"Array: {sample_array}")
print(f"Shape: {sample_array.shape}")
print(f"Size: {sample_array.size}")
print(f"Number of dimensions: {sample_array.ndim}")
print(f"Data type: {sample_array.dtype}")
print(f"Item size (bytes): {sample_array.itemsize}")
print(f"Total bytes: {sample_array.nbytes}")
print()

# Reshaping arrays
print("Reshaping arrays:")
original = np.arange(12)
print(f"Original 1D: {original}")

reshaped_2d = original.reshape(3, 4)
print(f"Reshaped to 2D:\n{reshaped_2d}")

reshaped_3d = original.reshape(2, 2, 3)
print(f"Reshaped to 3D:\n{reshaped_3d}")
print()

# Copying vs viewing arrays
print("Copying vs viewing arrays:")

base_array = np.array([1, 2, 3, 4, 5])

# View (shares memory)
view_array = base_array.view()
view_array[0] = 99
print(f"After modifying view: base={base_array}, view={view_array}")

# Copy (independent)
copy_array = base_array.copy()
copy_array[0] = 77
print(f"After modifying copy: base={base_array}, copy={copy_array}")
print()

# Converting between arrays and lists
print("Converting between arrays and lists:")

# Array to list
array_to_convert = np.array([1, 2, 3, 4, 5])
converted_list = array_to_convert.tolist()
print(f"Array to list: {converted_list}, type: {type(converted_list)}")

# List to array (already shown, but with different types)
string_list = ["a", "b", "c"]
string_array = np.array(string_list)
print(f"String array: {string_array}, dtype: {string_array.dtype}")
print()

# Handling different shapes
print("Handling different shapes:")

# Different length lists (will create object array)
uneven_lists = [[1, 2], [3, 4, 5], [6]]
uneven_array = np.array(uneven_lists, dtype=object)
print(f"Uneven lists: {uneven_array}")
print(f"Shape: {uneven_array.shape}")

# Padding to make rectangular
# (This is more advanced, but showing the concept)
padded = np.array([np.pad(lst, (0, 3-len(lst)), constant_values=0) for lst in uneven_lists])
print(f"Padded to rectangular:\n{padded}")
print()

# Memory efficiency comparison
print("Memory efficiency:")
import sys

large_list = list(range(1000))
large_array = np.array(large_list)

list_memory = sys.getsizeof(large_list)
array_memory = large_array.nbytes

print(f"Memory for list: {list_memory} bytes")
print(f"Memory for array: {array_memory} bytes")
print(f"Array is more memory efficient: {list_memory > array_memory}")
print()

# Performance comparison
print("Performance comparison:")
import time

# Large datasets
size = 1000000
list_data = list(range(size))
array_data = np.array(list_data)

# Sum operation
start = time.time()
list_sum = sum(list_data)
list_time = time.time() - start

start = time.time()
array_sum = np.sum(array_data)
array_time = time.time() - start

print(f"List sum time: {list_time:.4f} seconds")
print(f"Array sum time: {array_time:.4f} seconds")
print(f"Array is faster: {array_time < list_time}")
print()

# Practical data analysis examples
print("Data analysis examples:")

# Creating arrays from data
print("Creating arrays from sample data:")

# Sales data
sales_list = [1200, 1500, 1100, 1800, 1400]
sales_array = np.array(sales_list)
print(f"Sales data: {sales_array}")

# Temperature readings
temperatures = [20.5, 22.1, 19.8, 21.3, 23.0]
temp_array = np.array(temperatures)
print(f"Temperatures: {temp_array}")

# Student scores
scores_2d = [
    [85, 92, 78],  # Student 1
    [96, 88, 91],  # Student 2
    [79, 85, 83]   # Student 3
]
scores_array = np.array(scores_2d)
print(f"Student scores:\n{scores_array}")
print(f"Shape: {scores_array.shape} (students x subjects)")
print()

# Array creation best practices
print("Best practices for array creation:")
print("1. Use np.array() to convert lists to arrays")
print("2. Specify dtype when you need specific data types")
print("3. Use np.zeros(), np.ones() for initialization")
print("4. Use np.arange() and np.linspace() for sequences")
print("5. Check array properties (shape, dtype) after creation")
print("6. Use reshape() to change dimensions")
print("7. Be aware of memory sharing with views vs copies")
print("8. NumPy arrays are more efficient than lists for numerical data")

# Common pitfalls
print("\nCommon pitfalls to avoid:")
print("- Forgetting that arrays are mutable")
print("- Mixing incompatible data types unintentionally")
print("- Not checking array shapes before operations")
print("- Assuming arrays behave exactly like lists")

print("\nNumPy arrays creation demo completed!")
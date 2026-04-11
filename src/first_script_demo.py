# Demo for Creating and Running a First Python Script for Data Analysis

# This script demonstrates the basics of writing and running a Python script for data analysis.
# It covers importing libraries, loading data, performing simple calculations, and displaying results.

# First, we need to import the necessary libraries
# pandas is great for data manipulation
# numpy for numerical operations
# matplotlib for plotting (though we won't use it here for simplicity)

import pandas as pd
import numpy as np

# Define some sample data
# In a real scenario, this would come from a file
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'score': [85, 92, 78, 96]
}

# Create a DataFrame from the data
# DataFrame is like a table in pandas
df = pd.DataFrame(data)

# Display the data
print("Sample Data:")
print(df)
print()

# Perform some basic analysis
# Calculate the average age
average_age = df['age'].mean()
print(f"Average age: {average_age}")

# Calculate the average score
average_score = df['score'].mean()
print(f"Average score: {average_score}")

# Find the highest score
max_score = df['score'].max()
print(f"Highest score: {max_score}")

# Find who has the highest score
top_student = df.loc[df['score'].idxmax(), 'name']
print(f"Top student: {top_student}")
print()

# Add a new column: age group
# Categorize people as 'young' or 'adult'
df['age_group'] = df['age'].apply(lambda x: 'young' if x < 30 else 'adult')
print("Data with age groups:")
print(df)
print()

# Group by age group and calculate mean scores
grouped = df.groupby('age_group')['score'].mean()
print("Average scores by age group:")
print(grouped)
print()

# Simple statistics using numpy
ages_array = np.array(df['age'])
scores_array = np.array(df['score'])

print("Statistics using NumPy:")
print(f"Ages - Mean: {np.mean(ages_array)}, Std: {np.std(ages_array)}")
print(f"Scores - Mean: {np.mean(scores_array)}, Std: {np.std(scores_array)}")
print()

# Example of conditional analysis
# Find students with scores above average
above_average = df[df['score'] > average_score]
print("Students with above-average scores:")
print(above_average)
print()

# Save the results to a file
# This demonstrates output generation
output_file = "analysis_results.txt"
with open(output_file, 'w') as f:
    f.write("Data Analysis Results\n")
    f.write("====================\n\n")
    f.write(f"Average age: {average_age}\n")
    f.write(f"Average score: {average_score}\n")
    f.write(f"Highest score: {max_score}\n")
    f.write(f"Top student: {top_student}\n\n")
    f.write("Data with age groups:\n")
    f.write(df.to_string())
    f.write("\n\nAverage scores by age group:\n")
    f.write(grouped.to_string())

print(f"Results saved to {output_file}")

# This is the end of our first data analysis script
# To run this script, you would use: python first_script_demo.py
# Make sure you have pandas and numpy installed: pip install pandas numpy

# Additional examples to make the script longer

# Example 1: Working with different data types
print("\nExample 1: Data types")
print(f"Age column type: {df['age'].dtype}")
print(f"Name column type: {df['name'].dtype}")
print(f"Score column type: {df['score'].dtype}")
print()

# Example 2: Sorting data
print("Example 2: Sorting by score")
sorted_df = df.sort_values('score', ascending=False)
print(sorted_df)
print()

# Example 3: Filtering data
print("Example 3: Young students")
young_students = df[df['age'] < 30]
print(young_students)
print()

# Example 4: Adding calculated columns
print("Example 4: Adding normalized scores")
df['normalized_score'] = (df['score'] - df['score'].min()) / (df['score'].max() - df['score'].min())
print(df)
print()

# Example 5: Simple plotting (text-based)
print("Example 5: Simple score distribution")
for i, row in df.iterrows():
    stars = '*' * int(row['score'] / 10)
    print(f"{row['name']}: {stars} ({row['score']})")
print()

# Example 6: Error handling basics
print("Example 6: Basic error handling")
try:
    # This will work
    mean_age = df['age'].mean()
    print(f"Mean age calculated: {mean_age}")
except Exception as e:
    print(f"Error calculating mean: {e}")

try:
    # This might fail if column doesn't exist
    df['nonexistent'].mean()
except KeyError as e:
    print(f"Column not found: {e}")
print()

# Example 7: Functions (preview for later concepts)
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    else:
        return 'F'

print("Example 7: Adding grades")
df['grade'] = df['score'].apply(calculate_grade)
print(df)
print()

# Example 8: Working with lists (preview)
print("Example 8: Converting to lists")
names_list = df['name'].tolist()
ages_list = df['age'].tolist()
print(f"Names: {names_list}")
print(f"Ages: {ages_list}")
print()

# Example 9: String operations
print("Example 9: String operations")
df['name_upper'] = df['name'].str.upper()
print(df[['name', 'name_upper']])
print()

# Example 10: Summary statistics
print("Example 10: Full summary")
print(df.describe())
print()

print("First Python script demo completed!")
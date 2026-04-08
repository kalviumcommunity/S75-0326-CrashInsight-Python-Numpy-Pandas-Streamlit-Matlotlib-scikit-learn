# Demo for Creating a Project Folder Structure for Data Science Work

# In data science projects, organizing files and folders is crucial for efficiency and collaboration.
# A typical structure includes separate directories for data, source code, notebooks, outputs, and documentation.

# This script demonstrates how to create a basic project folder structure using Python's os module.
# It creates directories if they don't exist, simulating the setup of a new data science project.

import os

# Define the base directory for the project
# In a real project, this might be the current working directory or a specified path
base_dir = "demo_project"

# Create the base directory
# os.makedirs will create intermediate directories if they don't exist
os.makedirs(base_dir, exist_ok=True)

# Now, let's create subdirectories for different purposes

# 1. Data directory: This is where raw and processed data files are stored
# It's important to separate raw data (which shouldn't be modified) from processed data
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)

# Subdirectories under data
raw_data_dir = os.path.join(data_dir, "raw")
os.makedirs(raw_data_dir, exist_ok=True)

processed_data_dir = os.path.join(data_dir, "processed")
os.makedirs(processed_data_dir, exist_ok=True)

# 2. Source code directory: Contains Python scripts and modules
src_dir = os.path.join(base_dir, "src")
os.makedirs(src_dir, exist_ok=True)

# 3. Notebooks directory: For Jupyter notebooks used for exploration and analysis
notebooks_dir = os.path.join(base_dir, "notebooks")
os.makedirs(notebooks_dir, exist_ok=True)

# 4. Outputs directory: Where results, figures, models, and reports are saved
outputs_dir = os.path.join(base_dir, "outputs")
os.makedirs(outputs_dir, exist_ok=True)

# Subdirectories under outputs
figures_dir = os.path.join(outputs_dir, "figures")
os.makedirs(figures_dir, exist_ok=True)

models_dir = os.path.join(outputs_dir, "models")
os.makedirs(models_dir, exist_ok=True)

reports_dir = os.path.join(outputs_dir, "reports")
os.makedirs(reports_dir, exist_ok=True)

# 5. Documentation directory: For README files, documentation, etc.
docs_dir = os.path.join(base_dir, "docs")
os.makedirs(docs_dir, exist_ok=True)

# 6. Tests directory: For unit tests and integration tests
tests_dir = os.path.join(base_dir, "tests")
os.makedirs(tests_dir, exist_ok=True)

# 7. Configuration directory: For config files, environment settings
config_dir = os.path.join(base_dir, "config")
os.makedirs(config_dir, exist_ok=True)

# Print the created structure
print("Project folder structure created:")
print(f"Base directory: {base_dir}")
print("Subdirectories:")
for root, dirs, files in os.walk(base_dir):
    level = root.replace(base_dir, '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    subindent = ' ' * 2 * (level + 1)
    for d in dirs:
        print(f"{subindent}{d}/")

# Explanation of each directory's purpose
print("\nExplanation of the folder structure:")
print("- data/: Contains all data-related files")
print("  - raw/: Original, unmodified data files")
print("  - processed/: Cleaned and transformed data")
print("- src/: Source code, Python scripts and modules")
print("- notebooks/: Jupyter notebooks for data exploration")
print("- outputs/: Results and artifacts from the analysis")
print("  - figures/: Charts, plots, visualizations")
print("  - models/: Trained machine learning models")
print("  - reports/: Generated reports and summaries")
print("- docs/: Documentation, README, guides")
print("- tests/: Unit tests, integration tests")
print("- config/: Configuration files, environment variables")

# Additional tips for project organization
print("\nAdditional organization tips:")
print("- Use version control (Git) for all code and notebooks")
print("- Keep sensitive information (API keys, passwords) in config files, not in code")
print("- Use relative paths in scripts to make the project portable")
print("- Document the purpose of each file in comments or a README")
print("- Regularly backup important data and models")
print("- Use virtual environments for Python dependencies")

# Example of creating a simple file in each directory
# This demonstrates how files might be organized

# Create a sample README in docs
readme_path = os.path.join(docs_dir, "README.md")
with open(readme_path, 'w') as f:
    f.write("# Demo Data Science Project\n\nThis is a sample project structure.\n")

# Create a sample script in src
script_path = os.path.join(src_dir, "data_loader.py")
with open(script_path, 'w') as f:
    f.write("# Sample data loading script\n\nimport pandas as pd\n\n# Load data function\ndef load_data(file_path):\n    return pd.read_csv(file_path)\n")

# Create a sample notebook placeholder
notebook_path = os.path.join(notebooks_dir, "exploration.ipynb")
with open(notebook_path, 'w') as f:
    f.write('{\n "cells": [],\n "metadata": {},\n "nbformat": 4,\n "nbformat_minor": 4\n}')

print("\nSample files created in the structure.")

# Clean up: remove the demo directory (optional)
# import shutil
# shutil.rmtree(base_dir)
# print("Demo directory removed.")
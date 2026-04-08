# Demo for Organizing Raw Data, Processed Data, and Output Artifacts

# In data science, proper organization of data and outputs is essential for reproducibility and collaboration.
# Raw data should never be modified; instead, we create processed versions.
# Outputs like figures and models should be stored separately.

import os
import shutil
import pandas as pd

# Create a demo directory structure for this example
demo_dir = "data_organization_demo"
os.makedirs(demo_dir, exist_ok=True)

# Create subdirectories
raw_dir = os.path.join(demo_dir, "raw")
processed_dir = os.path.join(demo_dir, "processed")
outputs_dir = os.path.join(demo_dir, "outputs")

os.makedirs(raw_dir, exist_ok=True)
os.makedirs(processed_dir, exist_ok=True)
os.makedirs(outputs_dir, exist_ok=True)

# Simulate raw data: create a sample CSV file
raw_data_path = os.path.join(raw_dir, "raw_sales_data.csv")
raw_data = {
    'date': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'product': ['A', 'B', 'A'],
    'sales': [100, 150, 200]
}
df_raw = pd.DataFrame(raw_data)
df_raw.to_csv(raw_data_path, index=False)

print("Created raw data file:", raw_data_path)

# Processing step: clean and transform the data
# In a real scenario, this might involve handling missing values, normalizing, etc.
processed_data_path = os.path.join(processed_dir, "processed_sales_data.csv")

# Simple processing: add a total column
df_processed = df_raw.copy()
df_processed['total_with_tax'] = df_processed['sales'] * 1.1
df_processed.to_csv(processed_data_path, index=False)

print("Created processed data file:", processed_data_path)

# Generate outputs: a simple plot or report
# For demo, create a text report
report_path = os.path.join(outputs_dir, "sales_report.txt")
with open(report_path, 'w') as f:
    f.write("Sales Report\n")
    f.write("============\n")
    f.write(f"Total sales: {df_processed['sales'].sum()}\n")
    f.write(f"Average sales: {df_processed['sales'].mean()}\n")

print("Created output report:", report_path)

# Demonstrate the importance of organization
print("\nFile organization:")
print("Raw data (never modify):")
for file in os.listdir(raw_dir):
    print(f"  {file}")

print("Processed data (derived from raw):")
for file in os.listdir(processed_dir):
    print(f"  {file}")

print("Outputs (results and artifacts):")
for file in os.listdir(outputs_dir):
    print(f"  {file}")

# Best practices for data organization
print("\nBest practices:")
print("1. Keep raw data immutable")
print("2. Use version control for code, not for large data files")
print("3. Document data sources and processing steps")
print("4. Use consistent naming conventions")
print("5. Separate code, data, and outputs")
print("6. Backup important data regularly")

# Example of how NOT to organize (mixing everything)
bad_dir = os.path.join(demo_dir, "bad_organization")
os.makedirs(bad_dir, exist_ok=True)

# Copy files to bad directory (simulating poor organization)
shutil.copy(raw_data_path, os.path.join(bad_dir, "data.csv"))
shutil.copy(processed_data_path, os.path.join(bad_dir, "processed.csv"))
shutil.copy(report_path, os.path.join(bad_dir, "report.txt"))

print("\nPoor organization example (everything mixed):")
for file in os.listdir(bad_dir):
    print(f"  {file}")

# Clean up
# shutil.rmtree(demo_dir)

print("\nDemo completed. Remember to organize your data properly!")

# Additional examples and variations

# Example 1: Handling multiple data sources
print("\nExample 1: Multiple data sources")
# Create another raw data file
raw_data2_path = os.path.join(raw_dir, "raw_inventory_data.csv")
inventory_data = {
    'product': ['A', 'B', 'C'],
    'stock': [50, 30, 20]
}
df_inventory = pd.DataFrame(inventory_data)
df_inventory.to_csv(raw_data2_path, index=False)

# Process: merge sales and inventory
merged_path = os.path.join(processed_dir, "merged_sales_inventory.csv")
df_merged = pd.merge(df_raw, df_inventory, on='product', how='left')
df_merged.to_csv(merged_path, index=False)

print("Merged data created:", merged_path)

# Example 2: Creating different output types
print("\nExample 2: Different output types")
# Text summary
summary_path = os.path.join(outputs_dir, "summary.txt")
with open(summary_path, 'w') as f:
    f.write("Data Summary\n")
    f.write(f"Number of records: {len(df_merged)}\n")
    f.write(f"Unique products: {df_merged['product'].nunique()}\n")

# CSV export of summary stats
stats_path = os.path.join(outputs_dir, "stats.csv")
stats = df_merged.describe()
stats.to_csv(stats_path)

print("Additional outputs created:", summary_path, stats_path)

# Example 3: Organizing by date or category
print("\nExample 3: Organizing by categories")
# Create subdirectories in processed
monthly_dir = os.path.join(processed_dir, "monthly")
os.makedirs(monthly_dir, exist_ok=True)

# Simulate monthly processing
jan_data = df_processed[df_processed['date'].str.startswith('2023-01')]
jan_path = os.path.join(monthly_dir, "january_processed.csv")
jan_data.to_csv(jan_path, index=False)

print("Monthly data organized:", jan_path)

# Example 4: Backup strategy
print("\nExample 4: Backup considerations")
backup_dir = os.path.join(demo_dir, "backup")
os.makedirs(backup_dir, exist_ok=True)

# Copy important files to backup
shutil.copy(raw_data_path, os.path.join(backup_dir, "raw_backup.csv"))
shutil.copy(processed_data_path, os.path.join(backup_dir, "processed_backup.csv"))

print("Backup created for critical files")

# Example 5: Documentation
print("\nExample 5: Documentation")
readme_path = os.path.join(demo_dir, "README.md")
with open(readme_path, 'w') as f:
    f.write("# Data Organization Demo\n\n")
    f.write("This demo shows proper data organization practices.\n\n")
    f.write("## Directory Structure\n\n")
    f.write("- raw/: Original data files\n")
    f.write("- processed/: Cleaned and transformed data\n")
    f.write("- outputs/: Analysis results and reports\n")

print("Documentation created:", readme_path)

print("\nAll examples completed!")
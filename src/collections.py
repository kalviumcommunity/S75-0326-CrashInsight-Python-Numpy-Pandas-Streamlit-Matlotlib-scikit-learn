# Lists (mutable)

accidents = [10, 20, 15, 30]

print("Original list:", accidents)

# Access element
print("First element:", accidents[0])

# Modify element
accidents[1] = 25

# Add element
accidents.append(40)

# Remove element
accidents.remove(15)

print("Updated list:", accidents)

# Tuples (immutable)

coordinates = (10.5, 20.3)

print("Tuple:", coordinates)

# Access element
print("Latitude:", coordinates[0])

# Try modifying (this will fail)
# coordinates[0] = 99  # Uncomment to see error

# Dictionary (key-value pairs)

accident_data = {
    "location": "Highway",
    "weather": "Rainy",
    "time": "Night"
}

print("Dictionary:", accident_data)

# Access value
print("Weather:", accident_data["weather"])

# Add new key
accident_data["severity"] = "High"

# Modify value
accident_data["time"] = "Evening"

print("Updated dictionary:", accident_data)


# Comparison

print("\n--- Data Structure Summary ---")
print("List:", accidents)
print("Tuple:", coordinates)
print("Dictionary:", accident_data)
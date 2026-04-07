# Basic if statement

accidents = 25

if accidents > 20:
    print("High number of accidents")
    
    # if-else example

accidents = 15

if accidents > 20:
    print("High accidents")
else:
    print("Normal accidents")
    
    
# Multiple conditions

accidents = 20

if accidents > 25:
    print("Very High Risk")
elif accidents > 15:
    print("Moderate Risk")
else:
    print("Low Risk")
    
    
# String comparison

weather = "Rainy"

if weather == "Rainy":
    print("Risk is higher due to rain")
else:
    print("Normal conditions")
    
    
# Using AND

accidents = 30
weather = "Rainy"

if accidents > 20 and weather == "Rainy":
    print("Very high accident risk")
    
    
# Using OR

if accidents > 20 or weather == "Foggy":
    print("Risk condition triggered")
    
# Using NOT

is_night = False

if not is_night:
    print("It is not night time")
    
    
# Combined logic

accidents = 28
weather = "Rainy"
time = "Night"

if accidents > 25 and weather == "Rainy" and time == "Night":
    print("Critical Risk Condition")
elif accidents > 15:
    print("Moderate Risk")
else:
    print("Low Risk")
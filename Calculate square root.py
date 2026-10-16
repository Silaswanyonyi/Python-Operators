import math

# Get input from the user and convert it to a float to handle decimals
user_input = input("Enter a number to find its square root: ")
number = float(user_input)

# Check if the number is negative to prevent a ValueError
if number < 0:
    print("Error: Cannot calculate the square root of a negative number using standard math.")
    print("Tip: Use the 'cmath' module if you need complex numbers.")
else:
    result = math.sqrt(number)
    print(f"The square root of {number} is {result}")

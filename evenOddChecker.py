# Get user input
number = input("Please enter a number: ")
# Convert string into an Int
number = int(number)
# Check if even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

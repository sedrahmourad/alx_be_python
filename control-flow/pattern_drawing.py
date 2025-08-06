# pattern_drawing.py

# Prompt user for a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for each row
while row < size:
    # For loop to print asterisks in the current row
    for col in range(size):
        print("*", end="")
    # Print a newline after each row
    print()
    row += 1

    
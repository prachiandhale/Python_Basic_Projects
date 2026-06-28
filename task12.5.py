# Import required modules
import random
import math

# Function to perform all operations
def unique_numbers_program():

    # Create an empty set
    numbers = set()

    print("Enter 10 numbers:")

    # Take 10 numbers as input
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.add(num)   # Store unique numbers only
                break
            
            except:
                pass
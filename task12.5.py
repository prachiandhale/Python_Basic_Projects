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
            except ValueError:
                print("Invalid input! Please enter an integer.")
                
    try:
        # Convert set into tuple
        number_tuple = tuple(numbers)

        print("\nUnique Numbers (Set):", numbers)
        print("Tuple:", number_tuple)
        
         # Check if there are at least 3 unique numbers
        if len(number_tuple) >= 3:
            random_numbers = random.sample(number_tuple, 3)
            print("3 Random Numbers:", random_numbers)
        else:
            print("Less than 3 unique numbers available.")
        
    except:
        pass    


   
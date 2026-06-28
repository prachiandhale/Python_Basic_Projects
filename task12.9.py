import math
import random
from datetime import datetime

# Dictionary to store calculation history
history = {}

# Function for basic arithmetic
def basic_arithmetic():
    try:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Choose Operation: "))

        if choice == 1:
            result = num1 + num2
            operation = f"{num1} + {num2}"

        elif choice == 2:
            result = num1 - num2
            operation = f"{num1} - {num2}"

        elif choice == 3:
            result = num1 * num2
            operation = f"{num1} * {num2}"

        elif choice == 4:
            result = num1 / num2
            operation = f"{num1} / {num2}"

        else:
            print("Invalid Choice!")
            return

        print("Result:", result)

        # Store result with timestamp
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        history[time] = f"{operation} = {result}"

    except ZeroDivisionError:
        print("Cannot divide by zero.")

    except ValueError:
        print("Invalid Input! Please enter numbers only.")

    except Exception as e:
        print("Error:", e )
   
        
# Function for scientific calculations
def scientific_calculator():
    try:
        print("\n1. Square Root")
        print("2. Power")
        print("3. Factorial")

        choice = int(input("Enter Choice: "))

        if choice == 1:
            num = float(input("Enter Number: "))
            result = math.sqrt(num)
            operation = f"sqrt({num})"

        elif choice == 2:
            base = float(input("Enter Base: "))
            power = float(input("Enter Power: "))
            result = math.pow(base, power)
            operation = f"{base}^{power}"

        elif choice == 3:
            num = int(input("Enter Integer: "))
            result = math.factorial(num)
            operation = f"{num}!"

        else:
            print("Invalid Choice!")
            return

        print("Result:", result)

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        history[time] = f"{operation} = {result}"

    except ValueError:
        print("Invalid Input!")

    except Exception as e:
        print("Error:", e)
        
# Function to generate random numbers
def random_numbers():
    try:
        start = int(input("Enter Starting Number: "))
        end = int(input("Enter Ending Number: "))

        print("\nRandom Numbers:")
        nums = []

        for i in range(5):
            num = random.randint(start, end)
            nums.append(num)
            print(num)

        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        history[time] = f"Random Numbers: {nums}"

    except ValueError:
        print("Invalid Input!")

    except Exception as e:
        print("Error:", e)


    # Function to view history
def view_history():
    if len(history) == 0:
        print("No History Available.")
    else:
        print("\n===== HISTORY =====")
        for time, result in history.items():
            print(time, "->", result)
        
        
# Main Menu
while True:

    print("\n========== SMART CALCULATOR & DATA MANAGER ==========")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculator")
    print("3. Generate Random Numbers")
    print("4. View History")
    print("5. Exit")

    try:
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            basic_arithmetic()

        elif choice == 2:
            scientific_calculator()

        elif choice == 3:
            random_numbers()

        elif choice == 4:
            view_history()

        elif choice == 5:
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter a valid number.")
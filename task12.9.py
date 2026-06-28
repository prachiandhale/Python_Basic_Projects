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

        

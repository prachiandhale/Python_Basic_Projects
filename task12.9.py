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
        print("Error:", e)

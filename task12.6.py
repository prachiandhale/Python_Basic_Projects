# Lambda function to calculate square of a number
square = lambda x: x ** 2

try:
    # Generate numbers from 1 to 20
    numbers = range(1, 21)
    
     # Store squares in a list using lambda function
    square_list = list(map(square, numbers))
    
     # Print all squares
    print("Squares of numbers from 1 to 20:")
    print(square_list)
    
     # Print only even squares
    print("\nEven Squares:")
    for num in square_list:
        if num % 2 == 0:
            print(num, end=" ")

except Exception as e:
    # Handle any unexpected errors
    print("An error occurred:", e )
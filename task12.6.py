# Lambda function to calculate square of a number
square = lambda x: x ** 2

try:
    # Generate numbers from 1 to 20
    numbers = range(1, 21)
    
     # Store squares in a list using lambda function
    square_list = list(map(square, numbers))
    
except:
    pass
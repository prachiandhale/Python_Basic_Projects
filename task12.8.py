import math

try:
    # Take sentence as input
    sentence = input("Enter a sentence: ")

    # Check for empty input
    if sentence.strip() == "":
        raise ValueError("Sentence cannot be empty.")
    
except:
    pass
import math

try:
    # Take sentence as input
    sentence = input("Enter a sentence: ")

    # Check for empty input
    if sentence.strip() == "":
        raise ValueError("Sentence cannot be empty.")
    
    # Split sentence into words
    words = sentence.split()

    # Store unique words in a set (case-insensitive)
    unique_words = set(word.lower() for word in words)
    
except:
    pass
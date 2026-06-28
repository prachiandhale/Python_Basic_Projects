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
    
    # Sort the unique words
    sorted_words = sorted(unique_words)

    # Display unique words
    print("\nUnique Words (Sorted):")
    for word in sorted_words:
        print(word)
        
     # Count unique words
    total_unique = len(unique_words)

    # Print square of total unique words using math module
    print("\nTotal Unique Words:", total_unique)
    print("Square of Total Unique Words:", math.pow(total_unique, 2))
    
except:
    pass
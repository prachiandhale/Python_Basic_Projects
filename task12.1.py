# Function to analyze a string
def analyze_string(s):
    
    # Handle empty string case
    if len(s) == 0:
        print("Empty string entered!")
        return
    # Print length of the string
    print("Length of the string :", len(s))
    
     # Print string in reverse
    print("Reverse string :", s[::-1])
    
     # Count vowels (case insensitive)
    vowels = "aeiou"
    count = 0

    for ch in s.lower():
        if ch in vowels:
            count += 1

    print("Number of vowels :", count)

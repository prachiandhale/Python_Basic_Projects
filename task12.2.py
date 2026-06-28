# Function to manage student marks
def manage_marks():
     # Create an empty list to store marks
    marks = []

    print("Enter marks for 5 subjects:")

    # Take input for 5 subjects
    for i in range(5):
        while True:
            try:
                # Take numeric input
                mark = float(input(f"Enter marks for Subject {i + 1}: "))

                # Store mark in the list
                marks.append(mark)
                break

            except ValueError:
                # Handle invalid (non-numeric) input
                print("Invalid input! Please enter numeric marks only.")
                
     # Calculate average marks
    average = sum(marks) / len(marks)
    
    # Find highest and lowest marks
    highest = max(marks)
    lowest = min(marks)

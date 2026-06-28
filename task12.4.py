# Function to manage student database
def student_database():

    # Dictionary to store student records
    students = {}

    while True:
        print("\n===== STUDENT DATABASE MENU =====")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Display All Students")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        
        except:
            pass

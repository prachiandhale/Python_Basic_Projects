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
            
            if choice == 1:
                roll_no = input("Enter Roll Number: ")

                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                city = input("Enter City: ")

                # Add record using update()
                students.update({
                    roll_no: {
                        "Name": name,
                        "Age": age,
                        "City": city
                    }
                })

                print("Student record added successfully!")

        
        except:
            pass

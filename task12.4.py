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
                
            elif choice == 2:
                roll_no = input("Enter Roll Number to Search: ")

                # Search using get()
                record = students.get(roll_no)

                if record:
                    print("\nStudent Found")
                    print("Roll No :", roll_no)
                    print("Name :", record["Name"])
                    print("Age :", record["Age"])
                    print("City :", record["City"])
                else:
                    print("Student not found!")
                    
            elif choice == 3:
                if len(students) == 0:
                    print("No student records available.")
                else:
                    print("\n===== STUDENT RECORDS =====")
                    for roll_no, record in students.items():
                        print("----------------------------")
                        print("Roll No :", roll_no)
                        print("Name :", record["Name"])
                        print("Age :", record["Age"])
                        print("City :", record["City"])
                        
            elif choice == 4:
                print("Exiting Student Database...")
                break

            else:
                print("Invalid choice! Please select between 1 and 4.")

        
        except:
            pass

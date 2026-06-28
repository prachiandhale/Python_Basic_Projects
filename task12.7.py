class Employee:

    # Constructor to initialize employee details
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name

        # Store department and salary in a tuple
        self.details = (department, salary)
        
    # Method to display employee details
    def show_details(self):
        print("\nEmployee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.details[0])
        print("Salary      :", self.details[1])

employees = {}

# Add details of 3 employees
for i in range(3):
    print(f"\nEnter Details of Employee {i + 1}")

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    
    while True:
        try:
            salary = float(input("Enter Salary: "))
            break
        except ValueError:
            print("Invalid salary! Please enter a numeric value.")
    

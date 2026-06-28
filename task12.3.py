class Student:

    # Constructor to initialize student details
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.marks_list = []
        
     # Method to add marks
    def add_mark(self, mark):
        try:
            mark = float(mark)

            # Check if marks are within valid range
            if mark < 0 or mark > 100:
                raise ValueError("Marks should be between 0 and 100.")

            self.marks_list.append(mark)

        except ValueError as e:
            print("Invalid Input!", e)
            
            
     # Method to calculate average marks
    def get_average(self):
        if len(self.marks_list) == 0:
            return 0
        return sum(self.marks_list) / len(self.marks_list)


     # Method to display student information
    def display_info(self):
        print("\n----- Student Details -----")
        print("Name :", self.name)
        print("Roll No :", self.roll_no)
        print("Marks :", self.marks_list)
        print("Average :", self.get_average())
        
        
try:
    # Take student details
    name = input("Enter Student Name: ")
    roll_no = input("Enter Roll Number: ")

    # Create Student object
    student = Student(name, roll_no)

    # Take marks for 5 subjects
    print("\nEnter marks for 5 subjects:")
    for i in range(5):
        mark = input(f"Enter mark {i + 1}: ")
        student.add_mark(mark)

    # Display student details
    student.display_info()

except Exception as e:
    print("An unexpected error occurred:", e)
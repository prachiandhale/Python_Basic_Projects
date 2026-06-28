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

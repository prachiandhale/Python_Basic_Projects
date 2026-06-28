class Employee:

    # Constructor to initialize employee details
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name

        # Store department and salary in a tuple
        self.details = (department, salary)
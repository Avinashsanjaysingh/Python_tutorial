# Create a class programmer for storing information of few programmers working at microsoft.


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def employeeDetails(self):
        return f"Name: {self.name}, Position: {self.position}"
    
employee1 = Employee("Avinash", "SDE 1")
print(employee1.name)
print(employee1.employeeDetails())





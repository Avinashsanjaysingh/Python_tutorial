
class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def employeeDetails(self):
        # print(f"Name: {self.name}, Position: {self.position}")
        return f"Name: {self.name}, Position: {self.position}"
        # return f"{self.name} {self.position}"

        
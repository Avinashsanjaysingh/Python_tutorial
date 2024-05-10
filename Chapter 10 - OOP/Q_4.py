# Add a static method in problem 2 to greet the user with hello.

# import Q_1_class
from Q_1_class import Employee

employeeClass = Employee("Avinash", "SDE-1")

print(f"Hello, {employeeClass.name}!")


greeting = Employee("Avinash", "SDE-1")

print(f"Hello, {greeting.name}!\nYour position is {greeting.position}.")

print(f"Hello, {Employee("Avinash", "SDE-1").name}")



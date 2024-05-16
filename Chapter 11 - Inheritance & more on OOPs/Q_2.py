# Create a class pets from a class Animals and further create class Dog from pets. Add a method bark to class Dog.

class Animals:
    animals = ("This is animals class.")

class Pets(Animals):
    pets = ("This is pets class.")

class Dogs(Pets):
    def bark(self):
        print("Dog is barking")

c1 = Dogs()

print(c1.animals)
print(c1.pets)
print(c1.bark())



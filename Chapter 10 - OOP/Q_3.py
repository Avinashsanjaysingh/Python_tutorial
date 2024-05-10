# Create a class with a class attribute a; create an object from it and set a directly using object.a = 0. Does this change the class attribute?


class MyClass:
    a = 1

# Create an object of MyClass
obj = MyClass()

print(obj.a,obj)

# Set the class attribute 'a' directly using the object
obj.a = 0

# Check the class attribute 'a'
print("Class attribute 'a':", MyClass.a,obj.a,obj)


# In this code, we have a class 'MyClass' with a class attribute 'a' set to '1'. Then, we create an object 'obj' from this class and directly set its attribute 'a' to '0'. Finally, we print the class attribute a. The output will be 'Class attribute 'a': 1'.

# Setting 'obj.a = 0' creates an instance attribute 'a' for the object 'obj'. It doesn't change the class attribute 'a'. To change the class attribute, you would need to modify it directly using 'MyClass.a = 0'.


# Check that a tuple cannot be changed in python.



# Creating a tuple
my_tuple = (1, 2, 3)

# Attempting to change an element (this will raise an error)
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"TypeError: {e}")

# Attempting to add an element (this will raise an error)
try:
    my_tuple += (4, 5)
except TypeError as e:
    print(f"TypeError: {e}")

# Attempting to remove an element (this will raise an error)
try:
    del my_tuple[1]
except TypeError as e:
    print(f"TypeError: {e}")



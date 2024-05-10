# Can you change the self parameter inside a class to something else(say 'avinash'). Try changing self to 'slf' or 'avinash' and see the effects.


# In Python, `self` is just a convention and can be replaced with any valid variable name, though it's strongly recommended to stick with `self` for readability and consistency. Let's demonstrate this with a simple class:


class MyClass:
    def __init__(slf, x):
        slf.x = x

    def print_x(avinash):
        print(avinash.x)

# Create an instance of MyClass
obj = MyClass(5)

# Call the method using the modified 'self'
obj.print_x()


# In this example, I've changed `self` to `slf` in the `__init__` method and to `avinash` in the `print_x` method. The code still works perfectly fine, as long as you use the modified variable consistently within the class. However, this practice is strongly discouraged because it deviates from the standard conventions and can lead to confusion among other developers who read your code.


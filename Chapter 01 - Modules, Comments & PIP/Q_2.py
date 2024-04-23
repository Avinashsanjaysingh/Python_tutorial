# Use REPL and print the table of 5 using it.

''' REPL means Read-Eval-Print Loop, such as Python'''

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

'''The `f` in the `print` function in Python stands for "formatted string." It is used to create formatted strings, also known as f-strings, in which expressions inside curly braces `{}` are evaluated and replaced with their values.

Here's an example to illustrate:

```python
x = 5
print(f"The value of x is {x}")
```

In this example, the f-string allows you to embed the value of the variable `x` directly into the string. When you run this code, it will print:

```
The value of x is 5
```

Using f-strings is a convenient and readable way to create strings with dynamic content, especially when incorporating variables or expressions within the string. It was introduced in Python 3.6 and is a powerful feature for string formatting.'''
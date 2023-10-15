#### **Errors and Exceptions**

There are (at least) two distinguishable kinds of errors: _syntax errors_ and _exceptions_.

--

**Syntax Errors**

```python
while True print('Hello world')
```
```
File "<stdin>", line 1
	while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

--

**Exceptions**

- Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. 

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

--

[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) lists the built-in exceptions and their meanings.

---
#### **Examples 
for code that causes errors and crashes the application:**

--

In each of following cases, the Python interpreter will raise an exception that can be caught and handled using a `try-except` block, which prevents the program from crashing and allows for more graceful error handling.

--

1. **IndexError**: Trying to access an item at an invalid index in a list.

```python
my_list = [1, 2, 3]
element = my_list[5]  # IndexError: list index out of range
```

--

2. **ZeroDivisionError**: Occurs when you try to divide a number by zero.

```python
result = 10 / 0  # ZeroDivisionError: division by zero
```

--

3. **NameError**: Trying to access a variable that has not been defined yet.

```python
print(some_undefined_variable)  # NameError: name 'some_undefined_variable' is not defined
```

--

4. **TypeError**: Occurs when an operation or function is applied to an object of inappropriate type.

```python
result = '3' + 3  # TypeError: can only concatenate str (not "int") to str
```

--

5. **FileNotFoundError**: Trying to open a file that doesn't exist.

```python
with open('nonexistent_file.txt', 'r') as file:
    read_data = file.read()  # FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
```

--

6. **ValueError**: Raised when a built-in operation or function receives an argument that has the right type but an inappropriate value.

```python
number = int("not_a_number")  # ValueError: invalid literal for int() with base 10: 'not_a_number'
```

---

#### **Raising Exceptions**

- The [`raise`](https://docs.python.org/3/reference/simple_stmts.html#raise) statement allows the programmer to force a specified exception to occur. For example:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```

--

- If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:

```python
raise ValueError  # shorthand for 'raise ValueError()'
```

---

#### Exception handling

**How can you decide what to do when a particular exception (or exceptions) is raised?**

--

```python
try: # Mandatory Clause
	# do something that may throw (raise) an error

except <Exception Class> as <Exception Object Name>: # Mandatory Clause
	# do something instead of crashing the application

else: # optional clause
	# do something if your code didn't through an error
	# maybe print your result? save it? send it somewhere?

finally: # optional clause
	# clean up the mess you created in the try clause,
	# whether your code gave an error or not
```

--

```python
# 1. Current exceptions: Accessing the exception value
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Caught an exception: {e}")
```

--

```python
# 2. try & except: Basic exception handling
try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError:
    print("An error occurred!")
```

--

```python
# 3. try & except & else & finally: Code that runs if no exception occurs
def divide(x, y):
	try:
		result = x / y
	except ZeroDivisionError:
		print("division by zero!")
	else:
		print("result is", result)
	finally:
		print("executing finally clause")

```

--

```python
# 4. try & except & finally: Code in 'finally' will always be executed
try:
    file = open("file.txt")
except FileNotFoundError:
    print("File not found!")
finally:
    print("This block is executed no matter what.")
```

--

```python
# 5. Predefined cleanup actions with 'with'
try:
    with open("file.txt") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")
```

--

```python
# 6. Creating new exceptions: Custom exceptions can be created using classes
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom exception")
except CustomError as e:
    print(f"Caught an exception: {e}")
```

--

```python
# 7. Code that might raise different exceptions
try:
    x = 10 / 0
    lst = [1, 2, 3]
    value = lst[10]
except (ZeroDivisionError, IndexError) as e:
    print(f"Caught an exception: {e}")
```

---
#### **Predefined Clean-up Actions**

--

- Some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed.
- in the following example, which tries to open a file and print its contents to the screen.

```python
for line in open("myfile.txt"):
    print(line, end="")
```

--

- The problem with this code is that it leaves the file open for an indeterminate amount of time after this part of the code has finished executing.
- This is not an issue in simple scripts, but can be a problem for larger applications. 

--

- The [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

- After the statement is executed, the file _f_ is always closed, even if a problem was encountered while processing the lines.
- Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.

---




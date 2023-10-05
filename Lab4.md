

# Questions

--

**1. Objects vs Literals => Passing by Object References => Mutable vs Immutable:**

--

 **2. Global vs Local Variables => Scope and Namespace:**
 
- **Global Variables**: Variables declared outside functions or in the global scope.
	- They can be accessed anywhere in the code.
- **Local Variables**: Variables declared within a function. 
	- They can only be accessed within that function.

--

```python
global_var = 5

def my_function():
    local_var = 10
    print(global_var)  # Output: 5
    print(local_var)   # Output: 10

my_function()
print(global_var)  # Output: 5
print(local_var)   # Error: local_var is not defined
```

--

**3. For and While Loop:**
 
- **For Loop**: Iterates over a sequence (like a list or range) or other iterable objects.

```python
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
```

- **While Loop**: Repeats as long as a certain condition is true.

```python
i = 0
while i < 5:
    print(i)  # Output: 0, 1, 2, 3, 4
    i += 1
```

--

 **4. Range:**
- The `range()` function returns a sequence of numbers, starting from 0 by default, and increments by 1 by default, and stops before a specified number.

```python
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4
```

--

**5. Del:**
- The `del` statement is used to delete variables, elements of a list, slices, etc.

```python
x = [1, 2, 3, 4, 5]
del x[1]  # Deletes the item at index 1
print(x)  # Output: [1, 3, 4, 5]
```

--

 **6. Can you use a function before you define it? if yes, why? If no, why?**
```python
def outer_function():
    def inner_function():
        print("Inner function")

    inner_function()  # This is valid

outer_function()

inner_function()  # This will raise an error as inner_function is not defined in this scope.
```

--

**7. Bitwise Operators**
https://www.youtube.com/watch?v=5J4rWJHwLSE

---

# New Concepts

---
#### User Input and Evaluating Strings

```python
num = input('Enter a number: ')
print(num) # num is now a string so we should convert it to a number 
print(int(num))
```

```python 
num = int(input('Enter a number: '))
print(num) # num is now a number 
```

```python 
num = int('3+4') # will this work? 
num = eval('3+4') # eval can evaluate even expressions, provided the input is a string
```

---

#### Flow Control

![[Pasted image 20230927223301.png]]

--
##### If: 

```python
num1, num2 = 6, 5
if (num1 < num2):
    print("num1 is less than num2") # ? is it gonna print
```

```python
num1, num2 = 5, 6
if(num1 < num2): print("num1 is less than num2")
```

--
##### if else

```python
def password_check(password):
    if password == "Python@99>":
        print("Correct password")
    else:
        print("Incorrect Password")

password_check("Python@99>")
# Output Correct password

password_check("Python99")
# Output Incorrect Password
```

```python
hungry = True
x = 'Feed the bear now!' if hungry else 'Do not feed the bear.'
print(x)
```

--

##### if - elif - else

```python
num1, num2 = 5, 5
if(num1 > num2):
    print("num1 is greater than num2")
elif(num1 == num2):
    print("num1 is equal to num2")
else:
    print("num1 is less than num2")
```

--

##### using logical operators 

```python
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

```python
user = 'Arthur'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

---
#### Loops

```python
for element in sequence:
    body of for loop

while(condition):
	body of while loop
```
--
##### Loops with Lists

```python
# Example: Calculate the average of list of numbers

numbers = [10, 20, 30, 40, 50]

# definite iteration
# run loop 5 times because list contains 5 items
sum = 0
for num in numbers:
    sum = sum + num
list_size = len(numbers)
average = sum / list_size
print(average)
```

--

```python
# Example: Calculate the average of list of numbers
numbers = [10, 20, 30, 40, 50]
sum = 0
i = 0  # counter initialization
list_size = len(numbers)
while i < list_size:
    sum = sum + numbers[i]
    i = i + 1  # increment counter
average = sum / list_size
print(average)
```

--

##### Loops with Ranges
```python
# Example 7: printing a series of numbers using for and range

print("Case 1:")
for i in range(5):  # Print numbers from 0 to 4
    print (i)

print("Case 2:")
for i in range(5, 10):  # Print numbers from 5 to 9
    print (i)

print("Case 3:")
# Print numbers from 5 with distace 2 and stop before 10
for i in range(5, 10, 2): 
    print (i)
```
```
Case 1:
0
1
2
3
4
Case 2:
5
6
7
8
9
Case 3:
5
7
9
```

--

```python
print("Case 3:")

i = 5  # Start value

while i < 10:  # Stop value
    print(i)
    i += 2  # Step value

```

```python
print("Case 3:")

r = range(5, 10, 2)
i = 0  # initialize a counter

while i < len(r):
    print(r[i])
    i += 1  # increment the counter

```

--
##### Loops with other structures (iterables)

```python
person = {
    'first_name':'Milaan',
    'last_name':'Parmar',
    'age':96,
    'country':'Finland',
    'is_marred':True,
    'skills':['Python', 'Matlab', 'R', 'C', 'C++'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed ou

for value in dict1.values():
    print(value)
```

--

```python
	list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total=0
for list1 in list_of_lists:
    for i in list1:
        total = total+i
print(total)
```
```
45
```

--

```python
# Given tuple
my_tuple = (1, 2, 3, 4, 5)

# Square each element using a for loop and create a new tuple
new_tuple = tuple(item**2 for item in my_tuple)
print(new_tuple)  # Output: (1, 4, 9, 16, 25)

```

```python
# Given string
my_string = "hello"

# Capitalize each character using a for loop and create a new string
new_string = ''.join(char.upper() for char in my_string)
print(new_string)  # Output: HELLO
```

```python
# Given set
my_set = {1, 2, 3, 4, 5}

# Double each element using a for loop and create a new set
new_set = {item * 2 for item in my_set}
print(new_set)  # Output: {2, 4, 6, 8, 10}
```

--
##### Loop - else

```python
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number)
```
```
0
1
2
3
4
5
6
7
8
9
10
The loop stops at 10
```

--

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```
```
0
1
2
3
4
5
```

---
#### Transfer Statements

--
##### break

```python
# Example 1:

color = ['Green', 'Pink', 'Blue']
for i in color:
    if(i == 'Pink'):
        break
print (i)

# Example 1:

count = 0
while count < 5:
    if count == 3:
        continue
    else:
        print(count)
        count = count + 1
```

--

```python
# Example 2:

student_name = 'Arthur'

marks = {'Alan': 99, 'Bill': 55, 'Cory': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else: # ? run the else only when "break" is not executed
    print('No entry with that name found.')
#! but don't do that

# Example 2:

list = [60, "HelloWorld", 90.45, 50, 67.23, "Python"]  # total 6 elements
i = 0
while(i < 6):
    print(list[i])
    i = i + 1
    if(i == 3):
        break
```

--

##### continue

```python
# Example 3:

color = ['Green', 'Pink', 'Blue']
for i in color:
    if(i == 'Pink'):
        continue
print (i)
```

---

#### Enumerate vs Zip
##### enumerate

```python
# list of fruits
fruits = ["apple", "banana", "cherry"]

# using enumerate to loop through the list
for index, fruit in enumerate(fruits):
    print(f"Index {index} holds the fruit: {fruit}")

# Output:
# Index 0 holds the fruit: apple
# Index 1 holds the fruit: banana
# Index 2 holds the fruit: cherry

```

--
##### zip
```python
# list of fruits and their colors
fruits = ["apple", "banana", "cherry"]
colors = ["red", "yellow", "red"]

# using zip to loop through both lists in parallel
for fruit, color in zip(fruits, colors):
    print(f"The color of {fruit} is {color}")

# Output:
# The color of apple is red
# The color of banana is yellow
# The color of cherry is red

```
--

#### one-liners for loops (List Comprehension)

```python
first = [3, 6, 9]
second = [30, 60, 90]
final = []
for i in first:
    for j in second:
        final.append(i+j)
print(final)
```

--

```python
# Example 1: single line `for` loop code

first = [3, 6, 9]
second = [30, 60, 90]
final = [i+j for i in first for j in second]
print(final)
```

```python
final = [[x, y] for x in [30, 60, 90] for y in [60, 30, 90] if x != y]
print(final)
```
```
[[30, 60], [30, 90], [60, 30], [60, 90], [90, 60], [90, 30]]
```

---


# Questions

--

**Is Compilation faster than Interpretation? Why?**

--

**Is Python a scripting or a programming language?** 

--

**Python 2 vs Python 3**

--

**Where do you write Python code?** 

--

**Why do we use python?**

--

**Where do functions like print() come from ?** 

--

**How do you think 3 ** 3 ** 3 is evaluated?** 

--

**An example you can use python for ?** 

--

**indentation in python**

---

# Review
---
#### Data Types, and Conversions#1 

**Implicit Type Conversion vs Explicit Type Conversion**

*int() - float() - complex()*

--

```python
a = 3.7
b = 19.16
c = 3 + 27j
d = 3.7 + 3 # 6.7 # converts 

print(int(b))
print(float(a))
print(complex(a))
print(complex(b))
print(complex(a, b))
```

---
#### Data Types, and Conversions#2

**str()**

--

```python
# Example:
a = '''Apple'''
b = """Apple"""
c = 'Apple'
d = "Apple"
e = Apple     # ERROR
f = 15
g = str(f) #  now this is a string: "15"
h = float(g) # now this is a float: 15.0
```

---
#### Data Types, and Conversions#3
**Boolean** (1,0)

--

```python
#REMEMBER  True == 1   False == 0
x = (1 == True) # True
y = (1 == False) # False
a = True + 6 # 7
b = False + 90 # 90

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)
```


---
#### Collections, Subscript Operator, Slicing

 *Slicing doesn't include the last element*
 
 *Sets don't have a subscript operator*

--

```python
fruits1 = ["Banana", "Apple", "Strawberry"]       # list []
print(fruits1[0]) 
print(fruits1[0:3]) 

```


--

```python
fruits2 = ("Banana", "Apple", "Strawberry")      # tuple ()
print(fruits2[0])
print(fruits2[0:3]) # print 0, 1, 2

```

--

 *Sets are unordered collections, so indexing has no meaning*
 
``` python
fruits3 = {"Banana", "Apple", "Strawberry"}        # set {}
print(fruits3[0]) # ERROR
print(fruits3[0:3]) # ERROR

```

 *Hence, the slicing operator **`[]`** does not work.*
 
--

```python
# dictionary {"Key":"Value"}
fruits4 = {"1":"Banana", "2":"Apple", "3":"Strawberry"} 

print(fruits4['1'])
print(fruits4.keys())
print(fruits4.values())
```

--

```python
myString = 'Hello world!'
# s[4] = 'o'

print("length of the string myString is: " + len(myString))

print("s[4] = ", s[4])

print("s[6:11] = ", s[6:11]
# s[6:11] = 'world' 
# index '6' to '11' means element from 6 to 10

```

---

#### More on Slicing

```
**Syntax** of Slice Operator :

str[start : stop : step ]

other syntax of slice:

str[start : stop]  # items start through stop-1

str[start : ]      # items start through the rest of the array

str[ : stop]       # items from the beginning through stop-1

str[ : ]           # a copy of the whole array
```

**the default of step is 1**

--
##### Forward and Backward Indexing 

![](../Lab3-1.png)
```python
s = "Python is just ok"

print(s[6:10]) # " is "
print(s[-12:-7]) # "n is "
print(s[2: 10: 2]) #step = 2 => "to s"
print(s[ : 5])     #from 0 to 4 => "Pytho"
print(s[3 : ])     #from 3 to end of the string => "hon is just ok"

print(s[ : ])      #copy all string

print(s[-1: :-1])  #reversed all string 
print(s[ : : -1])  #reversed all string
print(s[-1:-len(s)-1:-1])  #reversed all string 
# -> start: -1, stop: -17 -1 = -18 
# (so now it includes the first letter), step is -1
```

---
#### Adding and Removing & Mutable vs Immutable

Lists are **mutable**, meaning, the value of elements of a list can be altered.

Just like lists, the slicing operator [ ] can be used with strings, and tuples. Both, however, are immutable.

--

```python
# Change the element of the List
a = [1, 2, 3]
#   [0  1  2] ➡ Index forward

a[2] = 4  
# Change my third element from '3' to '4' 
# [2] is the index number
print(a)
```

---
#### Escape Characters

 `\n`: Newline
 
 `\t`: Tab
 
 `\"`: Double quote
 
 `\'`: Single quote
 
 `\\`: Backslash

--

 
```python
print("Hello, World!\n")  # Outputs a newline after "Hello, World!"
print("Hello\tWorld!")    # Outputs a tab between "Hello" and "World!"
print("She said, \"Hello, World!\"")  # Outputs double quotes around "Hello, World!"
print('She said, \'Hello, World!\'')  # Outputs single quotes around "Hello, World!"
print("Backslash: \\")   # Outputs a single backslash: \
```
---


# New Concepts
---
#### String Formating

```python
name = "Ahmed"
print(f'Hi, my name is {name}')
```

```python
x = 6; y = 12
print('The value of x is {} and y is {}'.format(x,y))
	
print('Hello {name}, {greeting}!'
	  .format(greeting = 'Good morning', name = 'Mark'))

```

--

 **sprintf** 

```python
# %s => a string
# %i or %d => an integer
# %f => an integer

x = 12.34567890
print('The value of x is %0.2f' %x)  # "%0.2" means only 2 number after decimal

print('The value of x is %0.3f' %x)  # "%0.3" means only 3 number after decimal
```

for more details: [Python String Formatting Best Practices – Real Python](https://realpython.com/python-string-formatting/)

---
#### Classes vs Objects

 **What do you think of when you start creating a software?** 

1- performance 
2- memory & storage  
3- readability & reusability => this is why oop and functions are here 

--
#### OOP

![](../Lab3-2.png)

--

- **Programs consist of entities with different functionalities** 

- **Each entity provides an interface that allows the others to reach it** 

- **Every program actually simulates something in real life** 

- **What does your program do? Vs What things are in my program?**

--

**Everything in Python is an object**

```python
a = 6
print(a, "is of type", type(a))
print(a, "is integer number?", isinstance(5,int))

a = 3.0
print(a, "is of type", type(a))
print(a, "is float number?", isinstance(2.0,float))

a = 1+2j  # '1' is real part and '2j' is imaginary part
print(a, "is of type", type(a))
print(a, "is complex number?", isinstance(1+2j,complex))
```
```
6 is of type <class 'int'>
6 is integer number? True
3.0 is of type <class 'float'>
3.0 is float number? True
(1+2j) is of type <class 'complex'>
(1+2j) is complex number? True
``` 


---
#### More On Operators #1

![](../Lab3-3.png)

--

```python
print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)

# Division in python gives floating number
print ('Division: ', 4 / 2) 
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
# gives without the floating number
# or without the remaining
print('Division without the remainder: ', 7 // 2)   
print('Modulus: ', 3 % 2) # Gives the remainder
print('Exponential: ', 3 ** 2) # it means 3 * 3

```

```
Addition:  3
Subtraction:  1
Multiplication:  6
Division:  2.0
Division:  3.0
Division:  3.5
Division without the remainder:  3
Modulus:  1
Exponential:  9
```


---
#### More On Operators #2

![](../Lab3-4.png)

--


```python
print(6 > 3) # True, because 3 is greater than 2
print(6 >= 3) # True, because 3 is greater than 2
print(6 < 3) # False,  because 3 is greater than 2
print(3 < 6) # True, because 2 is less than 3
print(3 <= 6) # True, because 2 is less than 3
print(6 == 3) # False, because 3 is not equal to 2
print(6 != 3) # True, because 3 is not equal to 2
```
```
print(len("apple") == len("avocado"))  # False
print(len("apple") != len("avocado"))  # True
print(len("apple") < len("avocado"))   # True
print(len("banana") != len("orange"))  # False
print(len("banana") == len("orange"))  # True
print(len("tomato") == len("potato"))  # True
print(len("python") > len("coding"))   # Fals
```
---
#### More on Operators #3
![](../Lab3-5.png)

--

```python
x = 30
y = 22

print('x > y is',x>y)   # False
print('x < y is',x<y)   # True
print('x >= y is',x>=y) # False
print('x <= y is',x<=y) # Tru
```

--

```python
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False
```

```
True == True:  True
True == False:  False
False == False: True
True and True:  True
True or False: Tru
```

---
#### More on Operators #4
![](../Lab3-6.png)

--

```python
# True  - because the data values are the same
print('1 is 1', 1 is 1) 

# True  - because 1 is not 2
print('1 is not 2', 1 is not 2)

# False  - A is not found in the string
print('A in Milan', 'A' in 'Milan') 

# True  - a is not found in the string
print('A in Milan', 'a' in 'Milan') 


```

--

```python
# False - there is no uppercase B
print('B in Milan', 'B' in 'Milan') 
# True  becaues "python" is in python is fun
print('python' in 'python is fun') 

print('27 is 3 ** 3:', 27 is 3**3) # True
```

---
#### Precedence vs Associativity

 **Operator Precedence(Where to put my ()?)**
 **Associativity (From where to start?)**

[Precedence and Associativity of Operators in Python - GeeksforGeeks](https://www.geeksforgeeks.org/precedence-and-associativity-of-operators-in-python/)

--

1- " ( ) "

2- Exponentiation operator " ** "

3- Multiplication and Division 

4- Addition and subtraction 

5- Comparison and membership tests (in, not in, is, is not, <, <=, >, >=, !=, ==) 

6- " and " operator

7- " or " operator

--

*Associativity is the order in which an expression is evaluated that has multiple operators of the same precedence.*

```python
# Left-right associativity
# Output: 3
print(5 * 2 // 3)

# Shows left-right associativity
# Output: 0
print(5 * (2 // 3))

# Shows the right-left associativity of **
# Output: 512, Since 2**(3**2) = 2**9
print(2 ** 3 ** 2)

# If 2 needs to be exponated fisrt, need to use ()
# Output: 64
print((2 ** 3) ** 2

```

Almost all the operators have **left-to-right** associativity.

--

```python
# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
	print("Hello! Welcome.")
else:
	print("Good Bye!!")
```

```python
# Precedence of 'or' & 'and'
name = "Alex"
age = 0

if (name == "Alex" or name == "John") and age >= 2:
	print("Hello! Welcome.")
else:
	print("Good Bye!!")
```



---
#### New Keywords

**None**
```python
unInitializedVariable = None
```

**pass** 
```python
# Example 1:
for number in range(6):
    pass

pass
```
---
#### Iterables
![](../Lab3-7.png)

---
#### Conversions between collections, list(), set(), tuple()
```python
set([1,2,3])  # [1,2,3] is a list and now converting to a set {}
```
```
{1, 2, 3}
```

```python
tuple({5,6,7})  # {1,2,3} is set and now converting to a tuple ()
```
```
(5, 6, 7)
```

```python
list('hello')  # ("hello") is string and now converting to a list []
```
```
['h', 'e', 'l', 'l', 'o']
```

```python
dict([(3,63),(7,91)])  # [(3,63),(7,91)] is tuple and now converting to a dictionary
```
```
{3: 63, 7: 91}
```

---

[Lab3 Iterables]

---

### problemDescription#1
Create a simple program to manage a *library*'s **book** **inventory**. **Each book** *in the library* has the following information:

**- Title**
**- Author**
**- Year Published**
**- Copies Available**

### Data (Your variables)

###### What is your data?
**- Title**
**- Author**
**- Year Published**
**- Copies Available**

###### How would you present them?
**- Title**
		Example: "To Kill a Mockingbird"

**- Author**
		Example: "Harper Lee"

**- Year Published**
		Example: 1949

**- Copies Available**
		Example: 30

### Entities & Relationships (Collections)
###### **Book(s)**
1) **All** of them belong to a **library**
2) **Each** book has the following data:
**- Title**
			Example: "To Kill a Mockingbird"
			*This is a text so it should be a **String***

**- Author**
			Example: "Harper Lee"
			*This is a text so it should be a **String***

**- Year Published**
			Example: 1949
			*This is a number so it should be an **integer***

**- Copies Available**
			Example: 30
			*This is a number so it should be an **integer***
###### (A) Library
**All books belong the library**
#### How would you present your program?
###### **Book(s)**
> - *Book***s** will be a **list** of books
> - **A** *book* will be a **dictionary** that has "title", "author", "release_date", "copies" as **keys**

1) **All** of them belong to a **library**
2) **Each** book has the following data:
**- Title**
			Example: "To Kill a Mockingbird"
			*This is a text so it should be a **String***

**- Author**
			Example: "Harper Lee"
			*This is a text so it should be a **String***

**- Year Published**
			Example: 1949
			*This is a number so it should be an **integer***

**- Copies Available**
			Example: 30
			*This is a number so it should be an **integer***
###### (A) Library
**All books belong the library**
> - The *library* is my **script**

```python
myBooks = [
    {"title": "To Kill a Mockingbird", "author_year": ("Harper Lee", 1960), "copies": 4},
    {"title": "1984", "author_year": ("George Orwell", 1949), "copies": 6},
    # ... other books
]

print(myBooks)

```

    [{'title': 'To Kill a Mockingbird', 'author_year': ('Harper Lee', 1960), 'copies': 4}, {'title': '1984', 'author_year': ('George Orwell', 1949), 'copies': 6}]

### problemDescription#2
Create a simple program to manage a *library*'s **book** **inventory**.
 **Each book** *in the library* has the following information:

**- Title**
**- Author**
**- Year Published**
**- Copies Available**

#### Tasks
- The script should print the titles of the first 3 books
- The script asks a user for a year  
	- The script prints the total number of books in that year
	- The script prints all the books of that year

```python
myBooks = [
    {
	    "title": "To Kill a Mockingbird",
	    "author": "Harper Lee",
	    "year": 1960,
	    "copies": 4
	},
    {
	    "title": "1984",
	    "author": "George Orwell",
	    "year": 1949,
	    "copies": 6
	},
    # ... other books
]

###### Task #1
###### Print the library

#! get the first three books
firstThreeBooks = myBooks[0:3]

#! print the first three books
print(f"The first three books are {firstThreeBooks}")

###### Task #2
###### Find a book in the library

#! the program asks the user for a year
year_to_find = int(input("Please Enter a year to find: "))

#! the program filters the books to find the books with that year
found_books = []
for book in myBooks:
	if(book["year"] == year_to_find):
		found_books.append(book)

found_books_cnt = len(found_books)
print(f"The number of books found is: {found_books_cnt}")
print(f"The books of the year {year_to_find} are:\n{found_books}")


```

    The first three books are [{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'copies': 4}, {'title': '1984', 'author': 'George Orwell', 'year': 1949, 'copies': 6}]
    Please Enter a year to find: 1960
    The number of books found is: 1
    The books of the year 1960 are:
    [{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'copies': 4}]

### problemDescription#3
Create a simple program to manage a *library*'s **book** **inventory**. **Each book** *in the library* has the following information:
	***- Title**
	**- Author**
	**- Year Published**
	**- Copies Available***

#### Tasks
- The script should print the titles of the first 3 books
- The script asks a user for a year  
	- The script prints the total number of books in that year
	- The script prints all the books of that year
1) **Convert the code to use functions**

```python
myBooks = [
    {
	    "title": "To Kill a Mockingbird",
	    "author": "Harper Lee",
	    "year": 1960,
	    "copies": 4
	},
    {
	    "title": "1984",
	    "author": "George Orwell",
	    "year": 1949,
	    "copies": 6
	},
    # ... other books
]

def printLibrary(books):
	"""Print the library"""
	#! get the first three books
	firstThreeBooks = books[0:3]

	#! print the first three books
	print(f"The first three books are {firstThreeBooks}")

def findBooksByYear(year):
	"""Find a book in the library"""
	#! the program filters the books to find the books with that year
	global myBooks
	found_books = []
	for book in myBooks:
		if(book["year"] == year):
			found_books.append(book)
	return found_books

def main():
	###### Task #1
	printLibrary(myBooks)

	###### Task #2
	#! the program asks the user for a year
	year_to_find = int(input("Please Enter a year to find: "))

	books_to_find = []
	books_to_find = findBooksByYear(year_to_find)
	found_books_cnt = len(books_to_find)
	print(f"The number of books found is: {found_books_cnt}")
	print(f"The books of the year {year_to_find} are:\n{books_to_find}")

if __name__ == "__main__":
	main()

```

    The first three books are [{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'copies': 4}, {'title': '1984', 'author': 'George Orwell', 'year': 1949, 'copies': 6}]
    Please Enter a year to find: 1960
    The number of books found is: 1
    The books of the year 1960 are:
    [{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'copies': 4}]

2) **Make it able to handle errors**
```python
myBooks = [
    {
	    "title": "To Kill a Mockingbird",
	    "author": "Harper Lee",
	    "year": 1960,
	    "copies": 4
	},
    {
	    "title": "1984",
	    "author": "George Orwell",
	    "year": 1949,
	    "copies": 6
	},
    # ... other books
]

def printLibrary(books):
	"""Print the library"""
	if(len(books) == 0):
		print("The library is empty!!")

	#! get the first three books
	firstThreeBooks = books[0:3]

	#! print the first three books
	print(f"The first three books are {firstThreeBooks}")

def findBooksByYear(year):
	"""Return books from the library by year"""

	global myBooks
	#! the program filters the books to find the books with that year
	found_books = []
	for book in myBooks:
		if(book["year"] == year):
			found_books.append(book)

	return found_books

def main():
	###### Task #1
	printLibrary(myBooks)

	###### Task #2
	#! the program asks the user for a year
	year_to_find = int(input("Please Enter a year to find: "))

	books_to_find = []
	books_to_find = findBooksByYear(year_to_find)
	found_books_cnt = len(books_to_find)
	print(f"The number of books found is: {found_books_cnt}")
	print(f"The books of the year {year_to_find} are:\n{books_to_find}")

if __name__ == "__main__":
	main()

```

    The first three books are [{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'copies': 4}, {'title': '1984', 'author': 'George Orwell', 'year': 1949, 'copies': 6}]
    Please Enter a year to find: 1960
    The number of books found is: 1
    The books of the year 1960 are:
    [{'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960, 'copies': 4}]

### problemDescription#4
Create a simple program to manage a *library*'s **book** **inventory**.
 **Each book** *in the library* has the following information:
**- Title**
**- Author**
**- Year Published**
**- Copies Available**
#### Tasks
- The script should print the titles of the first 3 books
- The script asks a user for a year  
	- The script prints the total number of books in that year
	- The script prints all the books of that year

1) **Convert the code to use functions**
2) **Make it able to handle errors**
3) **Use classes and objects**
#### Entities & Relationships (Collections)

> The **design** is the **class**
> The **instances** are the **objects**
##### **(A) Book**
**Each** book has the following data:
**- Title**
			Example: "To Kill a Mockingbird"
			*This is a text so it should be a **String***

**- Author**
			Example: "Harper Lee"
			*This is a text so it should be a **String***

**- Year Published**
			Example: 1949
			*This is a number so it should be an **integer***

**- Copies Available**
			Example: 30
			*This is a number so it should be an **integer***

> There are no functions here because books don't do anything at this point
##### **(A) Library**

All books belong the library => **A library has a lot of books**
Functions:
	- You can print the library -> **printLibrary**
	- You can search in the library -> **findBooksByYear**

```python
class Library:
	"""
		A class to represent a library
		A library has a list of books
	"""
	def __init__(self):
		"""A constructor to initialize an object of a empty library"""
		self.books = []

	def addBook(self, book):
		self.books.append(book)

	def addBooks(self, newBooks):
		self.books.extend(newBooks)

	def printLibrary(self):
		"""Print the library"""
		if(len(self.books) == 0):
			print("The library is empty!!")

		#! get the first three books
		firstThreeBooks = self.books[0:3]

		#! print the first three books
		print(f"The first three books are {firstThreeBooks}")

		# if you don't define __repr__ then you can print this way
		#for book in firstThreeBooks:
		#		print(book)

	def findBooksByYear(self, year):
		"""Return books from the library by year"""
		found_books = []
		for book in self.books:
			if(book.year == year):
				found_books.append(book)
		return found_books

class Book:
	"""
		A class to represent a book
		A book has a title, author, year, copies
	"""
	def __init__(self, title, author, year, copies):
		"""A constructor to initialize an object of a book"""
		self.title = title
		self.author = author
		self.year = year
		self.copies = copies

	def __str__(self):
		details = ''
		details += f'Title        : {self.title}\n'
		details += f'Author    : {self.author}\n'
		details += f'Year : {self.year}\n'
		details += f'Copies : {self.copies}\n'
		return details

	def __repr__(self):
		return self.__str__()

def main():
	library1 = Library()

	mockingbird = Book("To Kill a Mockingbird", "Harper Lee", 1960, 4)
	book1984 = Book("1984", "George Orwell", 1949, 6)

	library1.addBook(mockingbird)
	library1.addBook(book1984)
	## library1.addBooks(
	## [mockingbird, book1984]
	## )

	#! print the library
	library1.printLibrary()

	#! the program asks the user for a year
	year_to_find = int(input("Please Enter a year to find: "))

	books_to_find = []
	books_to_find = library1.findBooksByYear(year_to_find)
	found_books_cnt = len(books_to_find)

	print(f"The number of books found is: {found_books_cnt}")
	print(f"The books of the year {year_to_find} are:\n{books_to_find}")

if __name__ == "__main__":
	main()

```

    The first three books are [Title        : To Kill a Mockingbird
    Author    : Harper Lee
    Year : 1960
    Copies : 4
    , Title        : 1984
    Author    : George Orwell
    Year : 1949
    Copies : 6
    ]
    Please Enter a year to find: 1960
    The number of books found is: 1
    The books of the year 1960 are:
    [Title        : To Kill a Mockingbird
    Author    : Harper Lee
    Year : 1960
    Copies : 4
    ]

### Questions For Next Class
#### Can you handle the errors better?
#### Can you split the application even more?




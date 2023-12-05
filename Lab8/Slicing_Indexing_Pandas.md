### Indexing 

### 1. Single Label
```python
import pandas as pd

# Sample DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Accessing a single column using a label
single_column = df['A']
print(single_column)
```
This will output the column `'A'` from `df`.

### 2. List of Labels
```python
# Accessing multiple columns using a list of labels
multiple_columns = df[['A', 'B']]
print(multiple_columns)
```
This will output both columns `'A'` and `'B'` from `df`.

### 3. Slice Object
```python
# Row slicing using a slice object
row_slice = df[0:2]
print(row_slice)
```
This will output the first two rows of `df`.

### 4. Boolean Array/Series
```python
# Using a boolean array for conditional indexing
condition = df['A'] > 1
filtered_df = df[condition]
print(filtered_df)
```
This will output rows of `df` where the values in column `'A'` are greater than 1.

### 5. Callable
```python
# Using a callable to select rows
callable_selection = df[lambda x: x['A'] > 1]
print(callable_selection)
```
This will output rows of `df` where the values in column `'A'` are greater than 1, similar to the boolean array example but using a lambda function.


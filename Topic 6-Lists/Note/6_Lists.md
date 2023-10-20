# Lists

[1. A list is a sequence](#1-a-list-is-a-sequence)    
&emsp;[Define a list](#define-a-list)  
&emsp;[`len()` function](#len-function)  
&emsp;[List slices](#list-slices)  
[2. Lists are mutable](#2-lists-are-mutable)  
[3. List methods](#3-list-methods)  
&emsp;[`.append()`](#append)  
&emsp;[`.extend()`](#extend)  
&emsp;[`.sort()`](#sort)  
[4. Void and fruitful method/function](#4-void-and-fruitful-methodfunction)  
[5. Traversing a list](#5-traversing-a-list)  
[6. List operations](#6-list-operations)  
&emsp;[`+` operator](#-operator)  
&emsp;[`*` operator](#-operator)  
&emsp;[`in` operator](#in-operator)  
[7. Deleting elements](#7-deleting-elements)


In Topic 4-Loop Part 4. List basics, we have discussed basics of lists:
- How to define a list
- How to access the elements in a list
- How to update the elements
- `range()` function gives us a range of numbers
- `len()` function to obtain length
In this part, we will study more about list, which is a useful and powerful container in Python .
## 1. A list is a sequence

### Define a list
- Like a string, a **list** is a sequence of values. In a string, the values are characters; in a list, the values can be any type. For example,
	```python
	>>> list_1 = [10, 20, 30, 40]
	>>> list_2 = ['Rutgers', 'Princeton', 'NYU']
	```
- In `list_1`, all values are number, or specifically `int`. In `list_2` all values are strings. 
- However, the elements in a list **are not necessarily the same type**. For example,
	```python
	>>> list_3 = [1, 3.14, 'Rutgers']
	```
- In the above list, we have `int`, `float`, and `string`
- We can even put a list into another list.
	```python
	>>> list_4 = [[1, 3.14], 'Rutgers']
	```
- In the above list, the first element is a list, which is `[1, 3.14]`; the second list is a string.
- So you can image that we can use a list to represent a matrix.
	```python
	>>> m = [[1,2,3],[4,5,6]]
	```

### `len()` function
- Just like strings, `len()` also works for lists. 
	```python
	>>> list_1 = [10, 20, 30, 40]
	>>> len(list_1)
	4
	```
### List slices
- List strings, the indices in list starts at 0.
	```python
	>>> l = ['a', 'b', 'c', 'd', 'e', 'f']
	>>> l[1:3]
	['b', 'c']
	```
- `l[1:3]` returns the elements with indices 1 and 2. It means it starts from 1 and stops at the index smaller than 3.
- If you omit the first index, the slice starts at the beginning.
	```python
	>>> l = ['a', 'b', 'c', 'd', 'e', 'f']
	>>> l[:4]
	['a', 'b', 'c', 'd']
	```
- If you omit the second, the slice goes to the end.
	```python
	>>> l = ['a', 'b', 'c', 'd', 'e', 'f']
	>>> l[3:]
	['d', 'e', 'f']
	```
- If you omit both, the slice is a copy of the whole list.
	```python
	>>> l = ['a', 'b', 'c', 'd', 'e', 'f']
	>>> l[:]
	['a', 'b', 'c', 'd', 'e', 'f']
	```

## 2. Lists are mutable
- Different from strings, lists are mutable.
	```python
	>>> l = ['a', 'b', 'c', 'd', 'e', 'f']
	>>> l[0] = 'w'
	>>> l
	['w', 'b', 'c', 'd', 'e', 'f']
	```
- We can also use slices to change the elements in a list.
	```python
	>>> l = ['a', 'b', 'c', 'd', 'e', 'f']
	>>> l[1:3] = ['x', 'y']
	>>> l
	['a', 'x', 'y', 'd', 'e', 'f']
	```

## 3. List methods

### `.append()`
- `append()` method adds a new element to the end of a list.
	```python
	>>> l = ['a', 'b', 'c']
	>>> l.append('d')
	>>> l
	['a', 'b', 'c', 'd']
	```

### `.extend()`
- `.extend()` takes a list as an argument and appends all of the elements:
	```python
	>>> l1 = ['a', 'b', 'c']
	>>> l2 = ['d', 'e']
	>>> l1.extend(l2)
	>>> l1
	['a', 'b', 'c', 'd', 'e']
	```

### `.sort()`
- `.sort()` sorts the list ascending by default. 
- There is an optional parameter, `reverse`, in `sort` method. Default is `reverse=False`. `reverse=True` will sort the list descending. 
- For strings:
	```python
	>>> l = ['d', 'b', 'a', 'c']
	>>> l.sort()
	>>> l
	['a', 'b', 'c', 'd']
	```
- For numbers:
	```python
	>>> l = [4, 10, 5, 2]
	>>> l.sort()
	>>> l
	[2, 4, 5, 10]
	```
- or
	```python
	>>> l = [4, 10, 5, 2]
	>>> l.sort(reverse=True)
	>>> l
	[10, 5, 4, 2]
	```


## 4. Void and fruitful method/function 
- Let us review methods in strings. Take `.upper()` for an example,
	```python
	name = 'jin'
	name = name.upper()
	print(name)
	```
- We will get the expected result, `JIN`. 
- Let us compare the string methods with the list methods below. Take the string `.append()` for an example,
	```python
	l = ['a', 'b', 'c']
	l.append('d')
	print(l)
	```
- Can you see the difference?
- **In string**, the method `.upper()` return a string, which is capitalized letters. 
- We call a function/method that returns values **fruitful function/method**, called a function that doesn't return values **void function/method**.
- **In list**, most methods are *void*; they modify the list and return None.
## 5. Traversing a list
- The most common way to traverse the elements of a list is with a for loop. The syntax is the same as for strings:
	```python
	universities = ['Rutgers', 'NYU', 'Princeton']
	for i in universities:
		print(i)
	```
- We can also traverse a list through indices.
	```python
	universities = ['Rutgers', 'NYU', 'Princeton']
	for i in range(len(universities)):
		print(universities[i])
	```

## 6. List operations
### `+` operator
- The + operator concatenates lists:
	```python
	>>> a = [1, 2, 3]
	>>> b = [4, 5, 6]
	>>> c = a + b
	>>> c
	[1, 2, 3, 4, 5, 6]
	```
### `*` operator
- The * operator repeats a list a given number of times:
	```python
	>>> [0] * 4
	[0, 0, 0, 0]
	>>> [1, 2, 3] * 3
	[1, 2, 3, 1, 2, 3, 1, 2, 3]
	```
### `in` operator
- The `in` operator helps find out whether an element is in a list.
	```python
	>>> universities = ['Rutgers', 'NYU', 'Princeton']
	>>> 'Rutgers' in universities
	True
	>>> 'Harvard' in universities
	False
	```

## 7. Deleting elements

**Method 1: `.pop()`** 
- If you know the index of the element you want, you can use pop:
	```python
	>>> t = ['a', 'b', 'c']
	>>> x = t.pop(1)
	>>> t
	['a', 'c']
	>>> x
	'b'
	```
- `pop` modifies the list and returns the element that was removed.

**Method 2: `del`**
- If you don’t need the removed value, you can use the `del` operator:
	```python
	>>> t = ['a', 'b', 'c']
	>>> del t[1]
	>>> t
	['a', 'c']
	```
- To remove more than one element, you can use del with a slice index:
	```python
	>>> t = ['a', 'b', 'c', 'd', 'e', 'f']
	>>> del t[1:5]
	>>> t
	['a', 'f']
	```

**Method 3: `.remove()`**
- If you know the element you want to remove (but not the index), you can use remove:
	```python
	>>> t = ['a', 'b', 'c']
	>>> t.remove('b')
	>>> t
	['a', 'c']
	```
- The return value from remove is None.


**To be continued**

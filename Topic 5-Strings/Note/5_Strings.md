# Strings


[1. A string is a sequence](#1-a-string-is-a-sequence)  
	[len function](#len-function)  
	[String slices](#string-slices)  
[2.  Strings are immutable](#2--strings-are-immutable)  
[3. String methods](#3-string-methods)  
	 [.strip()](#strip)  
	 [.title()](#title)  
	 [.upper()](#upper)  
[4. Traversal with a `for` loop](#4-traversal-with-a-for-loop)  
[5. Application 1: Searching](#5-application-1-searching)  
[6. Application 2: looping and counting](#6-application-2-looping-and-counting)  
[7. Practice questions](#7-practice-questions)


## 1. A string is a sequence
- We mentioned strings in Topic 1. We discussed string format, concatenation, repetition.
- In previous topics, we have mentioned several data types, i.e., integer, float, boolean, and strings. However, string is not like integer, float, and boolean. It is an ordered collection of other values.
- A string is a sequence of characters. You can access the characters one at a time with the bracket operator.
	```python
	>>> s = "Hello"
	>>> letter = s[1]
	>>> letter
	```
- The second statement selects character number 1 from `s` and assigns it to `letter`.
- The expression in brackets is called an *index*. The index indicates which character in the sequence you want. 
- But the result might not be what you expect. It is `e`, rather than `H`. It is because index starts from 0.
### len function
- Like list, we can use `len()` function of get the length of a string, i.e., the total number of characters in a string.
	```python
	>>> s = "Hello"
	>>> len(s)
	5
	```
- Note that the indices of a string are $0, 1, 2,  \cdots, n-1$, whether $n$ is the length of the string. Hence, to get the last letter of a string, you will get an error if you try something like this:
	```python
	>>> s = "Hello"
	>>> s[len(s)]
	IndexError: string index out of range
	```
- The reason for the `IndexError`  is that there is no letter in `Hello` with the index 5. The five letters in the string are indexed 0 to 4. So To get the last character, you have to subtract 1 from length:
	```python
	>>> s = "Hello"
	>>> s[len(s)-1]
	'o'
	```

### String slices
- A segment of a string is called a *slice*. Selecting a slice is similar to selecting a character, which can be done by using indices.
	```python
	>>> s = "Hello, Jin!"
	>>> s[0:5]
	```
- Guess which characters would be printed, the first five or six characters? That is, `0:5` includes indices, 0, 1, 2, 3, 4 or 0, 1, 2, 3, 4, 5? The answer is 0, 1, 2, 3, 4, and there is no 5. Hence, the output is "Hello", the first five characters.
-  You may have noticed that `n:m` includes the indices staring from `n` and stopping at `m-1`. For example, `2:5` includes 2, 3, and 4. For example:
	```python
	>>> s = "Hello, Jin!"
	>>> s[2:5]
	'llo'
	```
-  As an exercise, try to get `Jin`.
- In addition to the formula, `n:m`, you can also use `:m` and `n:`. If you omit the index before the colon, the indices start at 0.  If you omit the index after the colon, the indices stop at the end. For example
	```python
	>>> s = "Hello, Jin!"
	>>> s[:5]
	'Hello'
	>>> s[7:]
	'Jin!'
	```
- If the first index is greater than or equal to the second, the result is an empty string, represented by two quotation marks:
	```python
	>>> s = "Hello, Jin!"
	>>> s[3:3]
	''
	>>> s[3:2]
	''
	```

## 2.  Strings are immutable
- It is tempting to use the [] operator on the left side of an assignment, with the intention of changing a character in a string. 
	```python
	>>> s = "Hello, Jin!"
	>>> s[8] = 'o'
	TypeError: 'str' object does not support item assignment
	```
- An error occurs here saying 'str' object does not support item assignment. The “object” in this case is the string and the “item” is the character you tried to assign.
- The reason for the error is that strings are immutable, which means you can’t change an existing string.
- But you can get what you want in another way, creating a new string that is a variation on the original.
	```python
	>>> s = "Hello, Jin!"
	>>> new_s = s[:8] + 'o' + s[9:]
	```


## 3. String methods

### .strip()
- `input` function can be used for a user to input a string. But we cannot expect users will cooperate as intended. Hence, we need to either correct or check the input. For example:
	```python
	# ask user to input name
	name = input("Pleaser input your name: ")

	# print output
	print(f"Hello, {name}!")
	```
- It is common that users may mistakenly put extra spaces before or after their input. For example, run the program, then input `   Jin   ` (there are 3 white spaces before and after 'Jin'). The output would be `Hello,    Jin   !`
- It is fine, but awkward. We don't expect the white spaces. 
- A string built-in method `strip()` can strip all whitespaces on the left and right of a string. 
- We can modify the program to be:
	```python
	# ask user to input name
	name = input("Pleaser input your name: ")

	# Remove white spaces from the string
	name = name.strip()

	# print output
	print(f"Hello, {name}!")
	```
- Now if we input  `   Jin   ` , the output would be `Hello, Jin!` as expected. 

### .title()
- Again, in the name input example, users might just put small letters, for example, "jin", rather than "Jin" with capital letter at the beginning.
- We can use `.title()` method to capitalize the first letter of each word.
	```python
	# ask user to input name
	name = input("Pleaser input your name: ")

	# Remove white spaces from the string
	name = name.strip()

	# Capitalize the first letter of each word
	name = name.title()

	# print output
	print(f"Hello, {name}!")
	```
- If we input ` jin wang `, or even ` jIN wAng`, the output would be `Hello, Jin Wang!`
- You may be tired of adding methods. You can put the methods together to make the coding more efficient. You can get the same output as the previous code.
	```python
	# ask user to input name
	name = input("Pleaser input your name: ")

	# Remove white spaces from the string and Capitalize the first letter of each word
	name = name.strip().title()

	# print output
	print(f"Hello, {name}!")
	```
- Or even go further!
	```python
	# ask user to input name, Remove white spaces from the string, and Capitalize the first letter of each word
	name = input("Pleaser input your name: ").strip().title()

	# print output
	print(f"Hello, {name}!")
	```
### .upper()
- Similar to `.title()`, we can also use `.upper()` to capitalize all letters in a string.
	```python
	# ask user to input name, Remove white spaces from the string, and Capitalize the all letters
	name = input("Pleaser input your name: ").strip().upper()

	# print output
	print(f"Hello, {name}!")
	```
- If we input `jin`, the output would be `Hello, JIN!`

**.split()**
- The `split()` method splits a string into a list.
- We can specify the separator, default separator is any whitespace. For example, 
	```python
	# ask user to input name, including first name and last name
	name = input("Input first name, then last name (e.g., Jin Wang): ")

	# split the name into two parts
	x = name.split()

	# print output
	print(f"First name: {x[0]}")
	print(f"First name: {x[1]}")
	```
- In this program, if we input "Jin Wang", `x` value would be a list `['Jin', 'Wang']`
- We can  also specify the separator. For example,
	```python
	# ask user to input name, including first name and last name
	name = input("Input first name, then last name (e.g., Wang, Jin): ")

	# split the name into two parts
	x = name.split(',')

	# print output
	print(f"First name: {x[1].strip()}")
	print(f"First name: {x[0].strip()}")
	```
- We can obtain the same output as the previous code.

## 4. Traversal with a `for` loop
- A lot of computations involve processing a string one character at a time. 
- Often they start at the beginning, select each character in turn, do something to it, and continue until the end. 
- This pattern of processing is called a *traversal*. One way to write a traversal is with a while loop:
	```python
	s = "Hello"
	i = 0
	while i<len(s):
		letter = s[i]
		print(letter)
		i += 1
	```
- As an exercise, write a function that takes a string as an argument and displays the letters *backward*, one per line.
- Another way to write a traversal is with a for loop:
	```python
	s = "Hello"
	for l in s:
		print(l)
	```


## 5. Application 1: Searching
- With loop, we can do a lot of interesting operations on strings. For example, we can try to find out *whether there is a particular character in a string*. 
- Try to understand the following function.
	```python
	def find(word, letter):
		index = 0
		while index<len(word):
			if word[index] == letter:
				return index
			index = index + 1
		return -1		
	```
- This program takes a word and a character and finds the index where that character appears in the word. If the character is not found, the function returns -1.
- As an exercise, try to use `for` loop to implement the function. 

## 6. Application 2: Looping and counting
- We can also use loop to count the number of times a letter appears in a string. For example,
	```python
	word = 'banana'
	count = 0
	for letter in word:
		if letter == 'a':
			count = count + 1
	print(count)
	```
- This program demonstrates another pattern of computation called a counter. The variable count is initialized to 0 and then incremented each time an "a" is found.

## 7. Practice questions

1. Use two `input` function twice, one for inputing first name and another one for last name.  Use `.strip()` and `.title()` methods to correct user's input. Then print "Last name, First name". For example, input: " jin" as first name, "wang" as last name, the output would be "Wang, Jin".
2. Given an address, e.g., "100 Rockafeller Road, Piscataway, NJ 08854". Try to split the string, and get the information, street, city, state, zipcode.
3. Create a function, which takes a list of names and print "Hello, " together with each name. For example, taking a list, `['Mark', 'Peter', 'John']` , the function would print
	```python
	Hello, Mark
	Hello, Peter
	Hello, John
	```
4. Create a function, named `find_repetition`, to find out whether there are repetitive letters in a word. For example, For the word "Rutgers", the function returns `True` since the letter 'r' is repeated. (So it means we need to ignore the cases, 'R' is considered as a repetition of 'r'.) For the word "RBS", the function returns `False`.





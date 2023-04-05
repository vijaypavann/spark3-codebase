# Python Basics
Programming constructs that are helpful while developing Python/Spark Applications

#### Primitive Data Types
* str : Strings are used to represent text
    - Single Quotes `'AE'` OR Doube Quotes `"ad"` can be used to represent String Literal
	- Use triple quotes (""" or ''') for mulitline strings
		```python 
		'''first line
		some text
		third line
		'''
		```
	- f-strings: Formatted String - Used as an alternative for String concatenation 
			- available from Python >= 3.6 
			`f"This is {val} dynamic value replaced at runtime" ` instead of
			`"This is " + str(val) + "dynamic value replaced at runtime" `
			- Can be used for expression evaluation: `f"{5-78}"`
	- Escape the character using a backslash:
		` text = "Halo said, \"Hello!\""  `
	- Concatante: `"str1" + "str2" = "str1str2"`
	- Indexing: Starts with `0`, 
		```python
		text="Sample Text"
		text[3]
		text[0:3]  # substring 3 chars starting from 0
		```
		```danger  
		IndexError: string index out of range
		```
		```info
		Substring won't raise an IndexError even the index is out of boundaries of a String
		``` 
		- `"CRIC"[6:9]`
	- Negative Indexing: Last character has index `-1`
		|S|a|m|p|l|e| |C|o|l|
		-------------
		|-9||-8|-7|-6|-5|-4|-3||-2|-1|	
	- Immutable	
	- Repetition `"##"*4`
	- **String Methods **
		- `.lower()` `.upper()` `.strip()` `.lstrip()` `.rstrip()` `.startswith()` `.endswith()`
		- `.find()` - to find the index of substring
		   `"A given ex".find("ex")` **8**
* int - used to store whole numbers  `int("78")`
* float - used to store decimal points `int("123.9")`
##### Built-in Functions
 * len() - to get the length of a string including spaces <br\>
			`len(a bc)` **4**

* type() - function to determine the data type of a given value
			```python
			type("Hello, World")
			# <class 'str'>

			type(1.99)
			# float

			type(99)
			# int
			```
* input() - to take input from user
 `user_input = input("Enter your Name!") user_input.upper()`

* Looping
* Exceptions
* Lists, Tuples, Sets
* Dictionaries
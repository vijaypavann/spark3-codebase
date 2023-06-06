# Basics
Programming constructs that are helpful while developing Python/Spark Applications

---

## Primitive Data Types

- **`int`** - used to store whole numbers  

```python
	index = int("78")
	print(index, type(index), isinstance(index, int), sys.getsizeof(index) )
	# 78 <class 'int'> True 28
```

- **`float`** - used to store decimal points `float("123.9")`

- **`Boolean`** - used to store True / False values

```python
	is_valid: bool = True
	print(is_valid, type(is_valid), isinstance(is_valid, bool), sys.getsizeof(is_valid) )
	# True <class 'bool'> True 28
```

- **`str`** : Strings are used to represent text
    - Single Quotes `'AE'` OR Doube Quotes `"ad"` can be used to represent String Literal

	- Use triple quotes (""" or ''') for mulitline strings
		```python 
			''' 
				first line
				some text
				third line
			'''
		```

	- **f-strings**: Formatted String - Used as an alternative for String concatenation 
			- available from Python >= 3.6 

			* f"This is {val} dynamic value replaced at runtime"  instead of
			- "This is " + str(val) + "dynamic value replaced at runtime"  , 
			- "This is %s dynamic value replaced at runtime".format(str(val)) 

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

		!!!danger  Index Out of Range
			IndexError: string index out of range
		!!!

		!!! IndexError
			Substring won't raise an IndexError even the index is out of boundaries of a String
		!!! 

		- `"CRIC"[6:9]`

	- Negative Indexing: Last character has index `-1`

		|**String**|
		|-|
		|Positive Index|
		|Negative Index|

		| S|a|m|p|l|e|\\|c|o|l |
		| -------------------- |
		| 0|1|2|3|4|5|6|7|8|9 |
		| -10|-9|-8|-7|-6|-5|-4|-3|-2|-1 |	

	- Immutable	
		- value cannot be changed once it's created
		```python
			str_var = "python"
			str_var[0:3] = "abc"

			# TypeError   Traceback (most recent call last)
			# TypeError: 'str' object does not support item assignment
		```
	- del 
		- removes the references of the variable

	- Repetition 
	```python
		"-*~~*-"*4
		# '-*~~*--*~~*--*~~*--*~~*-'
	```

	- **String Methods**
		
		- `.lower()` `.upper()` `.strip()` `.lstrip()` `.rstrip()` `.startswith()` `.endswith()`

		- `.find()` - to find the index of substring

		-  `"A given ex".find("ex")` # Output: **8**

## Built-in Functions

 - **len()** - function to get the length of a string including spaces
			
```python
	len("a bc")
	# Output: 4
``` 

- **type()** - function to determine the data type of a given value
			
```python
	>>> type("Hello, World")
		# <type 'str'>
	>>> type(1.99)
		# <type 'float'>
	>>> type(99)
		# <type 'int'>
```

- **input()** - to take input from user. By default it is of `str` datatype

```md 
	user_input = input("Enter your Name!")
	user_input.upper()
```

- **sum()** - sum of elements in the list / set

- **min()** - min of elements in the list / set

- **max()** - max of elements in the list / set

- **enumerate()** - adds the index for the elements in the list / set

- **sorted()** - sorts the elements in the list / set

- **dir()** - function to list all the functions available  

```python
	>>> dir("abc")
		['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
	>>> dir(["a"])
		['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
	>>> dir(set)
		['__and__', '__class__', '__cmp__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'] 

```

---

## Lambda Functions

- Inline and are limited to a single expression
- Small anonymous functions that maintain no external state

	```python
		x = ['Python', 'programming', 'is', 'awesome!']
		print(sorted(x))
		print(sorted(x, key=lambda arg: arg.lower()))
		# Output: [ 'awesome!', 'is', 'programming', 'Python']
	```

* filter()
	```python
	x = ['Python', 'programming', 'is', 'awesome!']
	print(list(filter(lambda arg: len(arg) < 8, x)))
	# Output: ['Python', 'is']
	```

* map()
	```
	>>> x = ['Python', 'programming', 'is', 'awesome!']
	>>> print(list(map(lambda arg: arg.upper(), x)))
	['PYTHON', 'PROGRAMMING', 'IS', 'AWESOME!']
	```
* reduce()
	```
		from functools import reduce
		>>> x = ['Python', 'programming', 'is', 'awesome!']
		>>> print(reduce(lambda val1, val2: val1 + val2, x))
		Pythonprogrammingisawesome!
	```

---

## List, Tuples, Sets
### List 

* :: Features :: 
	- an ordered sequence of items
	- heterogenous datatypes can be stored
	- supports backward indexing, last index is -1

```python
	empty_list = []
	print(type(empty_list))
	# <class 'list'>

	hetro_list = ["abc", 1, 0.0, False]
	print(type(hetro_list))
	for val in hetro_list:
		print(val, type(val))
	# abc <class 'str'>
	# 1 <class 'int'>
	# 0.0 <class 'str'>
	# False <class 'bool'>

	nested_list = ["abc", 1, [20, 30], {"a", "b"}, {'k': 'v'}]
	print(type(nested_list))
	for val in nested_list:
		print(val, type(val))
	# <class 'list'>
	# abc <class 'str'>
	# 1 <class 'int'>
	# [20, 30] <class 'list'>
	# {'a', 'b'} <class 'set'>
	# {'k': 'v'} <class 'dict'>
```

* List Indexing

```python
	nested_list[3: ]
	# [[20, 30]]
	nested_list[2: 3]
	# [{'a', 'b'}, {'k': 'v'}]
```
* List Operations

```python
	nested_list.append("3") # returns NoneType
	nested_list
	# ['abc', 1, [20, 30], {'a', 'b'}, {'k': 'v'}, '3']

	nested_list.insert(3, 'd1') # returns NoneType
	nested_list
	# ['abc', 1, [20, 30], 'd1', {'a', 'b'}, {'k': 'v'}, '3', '3']

	nested_list.remove('d1') # throws ValueError if item not present in the list

	nested_list.pop() # Removes & returns the last item

	nested_list.pop(3) # Removes & returns the item at index 3
	# Returns IndexError if index out of range

	del nested_list[4] # Removes item at index 4

	# Re-assign / change the value in the list
	nested_list[0] = "eed"

	# Delete's all items in the list
	nested_list.clear()

	# Delete the list / removes the reference
	del nested_list

	# Check item present in list
	"abc" in nested_list

	# Sort, Reverse
	list = ['a', 'b', 'c'] 
	list.sort() # modifies the same list
	# list ['c', 'b', 'a']

	list.sort(reverse = True) # modifies the same list
	# list ['a', 'b', 'c'] 

	sorted(list) # returns a new list
	# ['c', 'b', 'a']

	# list ['c', 'b', 'a']
	list.reverse() # modifies the same list
	# ['c', 'b', 'a']

	list[::-1] # returns a new list
	# ['a', 'b', 'c']

	list.count("a") # 1  # Count of occurence of item

	all([1, 3, 0]) # False 

	any([1, 3, 0]) # True 
```

* Looping
	``` python
		for val in nested_list:
			print(val, type(val))

		# abc <class 'str'>
		# [20, 30] <class 'list'>
		# hlehlr <class 'str'>
		# {'a', 'b'} <class 'set'>
		# {'k': 'v'} <class 'dict'>
		#  3 <class 'str'>

		for indx, val in enumerate(nested_list):
			print(val, indx)

		# abc 0
		# [20, 30] 1
		# hlehlr 2
		# {'a', 'b'} 3
		# {'k': 'v'} 4
		# 3 5

	```


* List Copy

```python
	list = ['a', 'b', 'c'] 

	list_copy = list.copy()
	#  Creates a copy of list
	id(list_copy), id(list)
	# 4617619584, 4504640128

	list1 = list # references to the same list
	id(list1), id(4504640128)
	# 4504640128, 4504640128
 ```

* Join Lists
```python
	list_num = ["one", "two", "three"]
	list_indx = ["1", "2", "3"]

	new_list = list_num + list_indx # Creates a new list

	list_num.extend(list_indx) # Append list_indx to list_num

	"one" in list_num # Check `one` present in the list
```

* Reverse

```python
	list_num.reverse() # Reverse the list internally
	list_num
	# ['three', 'two', 'one']

	list_indx[::-1] # Returns the reversed list 
	# ['3', '2', '1']
	```

	* Sort List
	```python
	list_indx.sort() # Sorts the list in ascending order
	list_indx
	# ['1', '2', '3']

	list_indx.sort(reverse=True) # Sorts the list in descending order
	list_indx
	# ['3', '2', '1']


	sorted(list_indx) # Uses in built sorted()
	# ['1', '2', '3']
	```

	* Looping through a list
	```python
		for item in list_num:
			print(item)
		
		# three
		# two
		# one	

		for indx, item in enumerate(list_num):
			print(f"{indx} --> {item}")

		# 0 --> three
		# 1 --> two
		# 2 --> one

```

* Count, All, Any
```python
	list_num.count("one") #1

	all(list_indx)	# True as list doesn't contain 0 

	any(list_indx)	# True as list contains item other than 0 

	list_indx = [0, 1, 3]

	all(list_indx)	# False as list contains 0 

	any(list_indx)	# True as list contains element other than 0 
```


* List Comprehension
```python
	# Get all the lower case characters convert to upper & append using `,`
	from string import ascii_lowercase
	char_list = [char.upper() for char in ascii_lowercase]
	",".join(char_list)
	# 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'

   # Square of odd numbers
   doubled_list = [num ** 2 for num in range(10) if num % 2 != 0]
   doubled_list
   # [1, 9, 25, 49, 81]
```

##  Tuple
* Characteristics:
	-  Immutable values can't be changed once created
	- Used for holding multiple values 
	- faster iteration compared to list

```python
	tpl = () # empty tuple

	tpl2 = ("a", 1) # tuple with string & int values
	tpl2
	# ('a', 1)

	tpl3 = (1.4, 3.3, 4.5) # tuple with 3 values of floating data types
	len(tpl3) # 3

	tpl4 = (1, "3.3", [4, 5], {"1", "1", "2"} ) # tuple with 4 values of mixed data types

	for indx in tpl4:
    	print(indx, type(indx))

	# 1 <class 'int'>
	# 3.3 <class 'str'>
	# [4, 5] <class 'list'>
	# {'2', '1'} <class 'set'>

	tpl4[2][2] # tuple, list index starts with 0

	tpl4[:2] # # first 2 items in the tuple

	tpl4[-1] # # last item in the tuple

	tpl4.index("3.3") # 1 Index of element

```

## Sets
* Holds only unique values
* only Immutable values are allowed, 

```python
	nums = {4, 0, 8, 9, 4, 0}
	len(nums) # 4

	items = {4, [0, 8, 9], (4, 0, 5), "some text"}
	# TypeError: unhashable type: 'list'

	items = {4, (4, 0, 5), "some text"}
	for item in items:
		if type(item) == str or type(item) == tuple:
			print(item, len(item))
		else:
			print(item)
		# some text 9
		# 4
		# (4, 0, 5) 3

	items.add("NINE") 
	items # Adds to the same set

	items.update(["NINE", "NINE", "NINETO"]) 
	items # Adds the items in the list to the same set
	# {(4, 0, 5), 4, 'NINE', 'NINETO', 'some text'}
			
	items.remove("NINE") 
	items # Removes item `NINE` from the set 
	# {(4, 0, 5), 4, 'NINETO', 'some text'}

	items.discard("NINE") 
	items # same as remove

	items.clear() 
	items # Adds the items in the list to the same 		

	# Set operations
	# union, update, intersection, difference, issubset, issuperset, isdisjoint
```

## dict: Dictionary
	* Mutable data type {"key": "value"}
	* Keys must be unique, values can be duplicate

```python
	dummy_dict = dict() # Creates empty dict
	dummy_dict = {} # Creates empty dict

	int_dict = {1: "one", 2: "two"} # 
	int_dict = dic({1: "one", 2: "two"}) # 
	int_dict.keys() # dict_keys([1, 2])
	int_dict.values() # dict_values(['one', 'two'])

	for key, value in int_dict.items():
	    print(key, value)
	# 1 one
	# 2 two

	keys = {"a", "b", "c", "d"}
	str_dict = dict.fromkeys(keys)
	str_dict # {'c': None, 'd': None, 'b': None, 'a': None}

	keys = {"a", "b", "c", "d"}
	vals = [1, 3, 44]
	str_dict = dict.fromkeys(keys, vals)
	str_dict # {'c': [1, 3, 44], 'd': [1, 3, 44], 'b': [1, 3, 44], 'a': [1, 3, 44]}

	str_dict["d"] # [1, 3, 44]
	# KeyError: 'da' if key not present

	type(str_dict.get("da")) # NoneType 
	# doesn't throw Keyerror returns None
```

- `dict` can have mixed keys & nested types
    mixed keys 
	* `mixed_dict = {1: "one", '2': "two"}` # Mixed Keys 
	* `nested_dict = {1: "one", '2': ["two", 2]}` # Nested Dict

- Updating Items in `dict`
	* `row = {'name': 'PVN', 'id': 111, 'group': 'ABC'} `
	* row['id'] = 11
	* ``` 
		  item = {'group': 'MPC'}
	      row.update(item) 
	  ```	  
- Remove Items in `dict`
   * `row.pop("group")` # removes the item from the dict
   * `row.popitem()` # removes random item
   * del[row['id']]
   * row.clear() # Clears all the items

- All / Any
	- The all() method returns:
		- True - If all all keys of the dictionary are true
		- False - If any key of the dictionary is false
	- The any() function returns True if any key of the dictionary is True. If not, any() returns False

* Dict Comprehension

	``` python
		num_double = {num: num * 2 for num in range(10)} # double each value using dict comprehension
		num_double
		# {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}

		num_square = {num: num ** 2 for num in range(10)} # square each value 
		num_square
		# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

		keys = ['abc' , 'def' , 'ghi' , 'jkl' , 'mno']
		values = [1,2,3,4,5]
		str_dict = {k:v for (k,v) in zip(keys,values)} #
	```

---

* Looping
* Exceptions


## Modules
- **module** - contains reusable code builtin / custom
```python
import sys
import keyword
import operator
from datetime import datetime
import os

>>> print(keyword.kwlist) # List all Python Keywords
['and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while', 'with', 'yield']

>>> len(keyword.kwlist)
31
```
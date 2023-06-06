# Intro
Introduction to Programming Basics !!!

### Identifiers
- Name given to variables / classes / functions for unique identification
```python
my_var = "custom_string"
temp = 89.34
index = 2324
ref = MyCustomClass()
```

### Comments
- to exclude the code from execution 
- for writing code comments
```python
	# Single line Comment
	str_val = "A line of Code"
	
	#	Multi 
	#	Line
	#	Comment
	temp = "98.3F"
```

### Statements
```python
	var1 = ["a", "b", "c"] # Create a list and assign to identifier `var1`
	sum = 1 + 3 \
	      + 44 \
		  + 56
	sum = (1 + 3
			+ 44 
			+ 56)	  
```

### Indentation
- Spaces at the beginning of each code line. 4 spaces are recommended

```python
	var1 = ["a", "b", "c"] # Create a list and assign to identifier
	for value in var1:
		print(value) 
```	

### Docstrings
- To add documentation within functions, classes or modules

```python
class Demo():
    """
    Utility class used to demo the features available
    :param1: int value to initialize
    """
    def __init__(self, param1: int, param2: str):
        self.param1 = param1
        self.param2 = param2
        print(self.__dict__)

	if __name__ == "__main__":
    	obj = Demo(1, "abc") 
		print(obj.__doc__)
		# Output: '\n    Utility class used to demo the features available\n    :param1: int value to initialize\n    '

```	

### Variables
- reserved memory location to store the value

```python
param1 = "First Parameter Value"
print(param1, type(param1), id(param1), hex(id(param1)) )
# Output: First Parameter Value <class 'str'> 4587112048 0x11169c670

param1, param2, param3 = "First", 2, 0.33
print(param1, type(param1), param2, type(param2),param3, type(param3) )
# Output: First <class 'str'> 2 <class 'int'> 0.33 <class 'float'>
```
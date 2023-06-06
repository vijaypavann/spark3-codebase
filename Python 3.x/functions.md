# Functions

    - A function is a block of organized code written to carry out a specified task.
    - Functions help break our program into smaller and modular chunks for better readability.
    -  Information can be passed into a function as arguments.
    - Parameters are specified after the function name inside the parentheses.
    - We can add as many parameters as we want. Parameters must be separated with a comma.
    - A function may or may not return data.
    - In Python a function is defined using the `def` keyword

## Parameter VS Argument
- A parameter is the variable listed inside the parentheses in the function definition.
- An argument is the value that is sent to the function when it is called.
- Three types of functions in Python:-
    - **Built-in function** :- Python predefined functions that are readily available for use like `min()` , `max()` , `sum()` , `print()` etc.
    - **User-Defined Functions**:- Function that we define ourselves to perform a specific task.
    - **Anonymous functions** : Function that is defined without a name. Anonymous functions are
also called as `lambda functions`. They are not declared with the `def` keyword.

- Syntax
    ``` python
        def function_name(params: type) -> <RETURN_TYPE> :
            """
                Document String
            """
            statement(s)
            return <EXPRESSION>
    ```
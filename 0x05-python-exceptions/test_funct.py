def execute_function(func, *args, **kwargs):
    """Executes the given function with provided arguments.

    Args:
        func (function): The function to be executed.
        *args: Variable length argument list.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        Any: Result of executing the function.
    """
    try:
        result = func(*args, **kwargs)
        return result
    except Exception as e:
        return f"Error occurred: {e}"

# Example functions to be executed
def add(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

# Usage of execute_function to execute add() and greet() functions
add_result = execute_function(add, 5, 3)
print("Result of add:", add_result)

greet_result = execute_function(greet, "Alice")
print("Greeting:", greet_result)


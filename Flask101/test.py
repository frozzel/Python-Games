# TODO: Create the logging_decorator() function 👇

def logging_decorator(function):
    def wrapper(*args, **kwargs):
        function_name = function.__name__
        sum = function(*args, **kwargs)
        print(f'You called {function_name}\n It returned: {sum}')
    return wrapper
    
        

# TODO: Use the decorator 👇
@logging_decorator
def a_function(*args):
    return sum(args)
    
a_function(1,2,3)

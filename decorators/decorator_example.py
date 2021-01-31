def example_decorator(func):
    def wrapper(x,y):
        print("Do something before the function is called")
        func(x,y)
        print("Do something after the function is called")
    return wrapper

def clunky_wrapped_function(x,y):
    print(x+y)

clunky_wrapped_function(3,4)

clunky_wrapped_function = example_decorator(clunky_wrapped_function)
clunky_wrapped_function(5,6)

@example_decorator
def sleek_wrapped_function(a,b):
    print(a * b)

sleek_wrapped_function(5,9)

# # At this point, I wanted to make some decorators in a different file and use them in this file
from decorators import call_twice_decorator, double_argument_decorator, reverse_argument_decorator

@call_twice_decorator
def do_twice_function():
    print("PRINT ME TWICE")

do_twice_function()

@double_argument_decorator
def print_arg_doubled(i):
    print(i)

print_arg_doubled(5)
print_arg_doubled(25)
print_arg_doubled("doop")

@reverse_argument_decorator
def print_arg_reversed(arg):
    print(arg)

print_arg_reversed([1,2,3])
print_arg_reversed('GAMESTONK')
print_arg_reversed(123)

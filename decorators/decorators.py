def call_twice_decorator(func):
    def my_wrapper():
        func()
        func()
    return my_wrapper


def double_argument_decorator(func):
    def double_arg_wrapper(i):
        i *=2
        func(i)
    return double_arg_wrapper

def reverse_argument_decorator(func):
    def reverse_argument_wrapper(arg):
        if type(arg) == str:
            arg = arg[::-1]
            func(arg)
        elif type(arg) == list:
            arg.reverse()
            func(arg)
        else:
            print("Hey dude, I haven't programmed this decorator to reverse anything but strings and lists!")
            print("You passed in a",type(arg),"which I have not programmed to be handled yet. Sorry!") 
            func(arg)
    return reverse_argument_wrapper
x = lambda a : a + 10
print(x(5))

derp = lambda value: print("The value you passed in was", str(value))
derp(2)

foo = (lambda x: x * x)(7)
print(foo)

two_argument_addition = lambda x,y: x + y
print(two_argument_addition(4,9))

three_argument_addition = lambda x,y,z: x + y + z
print(three_argument_addition(1,7,3))


higher_order_func = lambda x, func: x + func(x)
test_value = higher_order_func(10, lambda y: y*y)
print(test_value)
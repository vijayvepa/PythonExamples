def custom_print(some_function, value):
    value = some_function(value)
    print(value)


custom_print(lambda x: x * 2, 5)
custom_print(lambda x: x * x, 24)

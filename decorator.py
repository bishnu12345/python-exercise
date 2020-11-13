def display_name():
    print('Apoorba')


def decorator_display_name(func_name):
    def wrapper_funtion():
        print('Added Code')
        func_name()
        print('Ended adding code')
    return wrapper_funtion  # returns wapper_function object


print('before using decorator')
display_name()
print('after using decorator')
modified_value = decorator_display_name(display_name)
modified_value()  # function is called and executed


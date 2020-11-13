def decorator_sum(sum):
    def wrapper_function():
        print('Addition result')
        sum()
    return wrapper_function

@decorator_sum
def sum():
    print(5+5)

sum()


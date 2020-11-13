def square(n):
    return n*n


num1 = [2, 3, 4]

results = map(square, num1)
print(list(results))

# Using map
num2 = [1, 2, 3]
results = map(lambda x: x**2, num2)
print(list(results))


number1 = [2, 8, 10]
number2 = [3, 7, 1]

results = map(lambda x, y: x+y, number1, number2)
print(list(results))

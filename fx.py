'''def greet(name):
    return f"Welcome back {name}"


greet('ahmed')


def increase(x, y):
    return x+y


solution = increase(2, 20)
print(solution)'''


def multiply(*numbers):
    total = 1
    for number in numbers:
        total += number
    return total


final = multiply(1, 2, 3, 4, 5)
print(final)

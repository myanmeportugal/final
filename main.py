# 1. Functions
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Invalid! Can't divide by zero!"
    elif b > a:
        return "Invalid! Can't divide small number by greater number!"
    return a / b


# 2. Variables & Prints
a = 10
b = 15

print("The sum of", a, "and", b, "is", add(a, b))
print("The difference of", a, "and", b, "is", sub(a, b))
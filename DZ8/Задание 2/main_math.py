def square (a :int):
    return a ** 2

def cube (a:int):
    return a ** 3

def is_even(a:int):
    if a % 2 == 1:
        return "Делится без остатка"
    return "Не делится без остатка"   

def factorial(a:int):
    if a <= 1:
        return 1
    return a * factorial(a-1)

def max_of_two(a:int,b:int):
    if a > b:
        return a
    return b
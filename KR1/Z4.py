def process_numbers(numbers, operation):
    return [operation(x) for x in numbers]

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    return abs(x)

numbers = [1, 2, 3, 4]

result_sq_l = process_numbers(numbers, lambda x: x ** 2)
print("Квадрат с модной  лямбдой:", result_sq_l)

result_cube_l = process_numbers(numbers, lambda x: x ** 3)
print("Куб с неповторимой  лямбдой:", result_cube_l)

result_abs_l = process_numbers(numbers, lambda x: abs(x))
print("Модуль с дерзкой лямбдой: ", result_abs_l)

result_sq = process_numbers(numbers, square)
print("Квадрат:", result_sq)

result_cube = process_numbers(numbers, cube)
print("Куб:    ", result_cube)

result_abs = process_numbers(numbers, absolute)
print("Модуль: ", result_abs)
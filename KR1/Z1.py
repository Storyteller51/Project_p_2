numbers = [int(x) for x in input("Введите числа через пробел: ").split()]

maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num

minimum = numbers[0]
for num in numbers:
    if num < minimum:
        minimum = num

right_sum = 0
for num in numbers:
    if num > 0:
        right_sum += num

print("Максимальное число:", maximum)
print("Минимальное число:", minimum)
print("Сумма положительных чисел:", right_sum)

final = sorted(set(numbers))
print("Уникальные числа по возрастанию:", final)
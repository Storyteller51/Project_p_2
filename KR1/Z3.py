grades = [78, 91, 56, 83, 95, 61, 88]

joska = list(map(lambda x: x + 5, filter(lambda x: x >= 60, grades)))
print(joska)
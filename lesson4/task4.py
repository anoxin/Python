# Задача 4 Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

num = int(input("Введите степень k = "))


def creatPolynomial(num):
    polynomial = ""
    for i in range(num, -1, -1):
        randomNumber = random.randint(1, 100)
        if (i > 1):
            polynomial += f'{randomNumber}x^{i} + '
        if (i == 1):
            polynomial += f'{randomNumber}x + '
        if (i < 1):
            polynomial += f'{randomNumber} = 0'

    return polynomial


f = open('text.txt', 'w')
f.write(creatPolynomial(num))
f.close()

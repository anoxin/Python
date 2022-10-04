# Задание 1. Вычислить число c заданной точностью d

# Пример:
# - при $d = 0.001, π = 3.141.$    $10 ^ {-1} >= d >= 10 ^ {-10}$
import math


def numberWithGivenPrecision(d, num):
    if (10**(-1) >= d >= 10**(-10)):
        d = int(len(str(d)[(str(num).find('.'))+1: len(str(d))]))
        num = float(str(num)[0: (str(num).find('.'))+1+d])
        return num
    else:
        return "Введены неверные данные"


print(numberWithGivenPrecision(0.001, math.pi))

# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример: *

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


num = int(input("Введите число "))


def convertDecimalToBinary(num):
    binary = ""
    while (num >= 2):
        binary = str(num % 2) + binary
        num = int(num / 2)
    return int(str(num) + binary)


print(convertDecimalToBinary(num))

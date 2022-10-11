# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

num = [x for x in range(1, int(input("Введите число ")) + 1)]


def multiplicationNumbers(num):
    for i in range(1, num):
        num *= i
    return num


myList = list(map(lambda x: multiplicationNumbers(x), num))
print(myList)

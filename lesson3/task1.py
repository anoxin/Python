#  Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример: *

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

myList = list(map(int, input("Введите числа через пробел ").split()))


def sumOfElements(myList):
    sum = 0
    for i in range(len(myList)):
        if (i % 2):
            sum += myList[i]
    return sum


print(sumOfElements(myList))

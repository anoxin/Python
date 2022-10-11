# Задача 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

myList = input("Введите числа через пробел ").split()

sum = sum(list(map(lambda x: int(x[1]), list(
    filter(lambda x: x[0] % 2 != 0, enumerate(myList))))))

print(sum)

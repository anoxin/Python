# Задача 3 Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

myList = list(map(int, input("Введите два числа через пробел ").split()))


def squareNumber(myList):
    newList = list(map(lambda x: x*x, myList))
    return newList[0] == myList[1] or newList[1] == myList[0]


print(squareNumber(myList))

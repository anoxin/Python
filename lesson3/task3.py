# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

myList = list(map(str, [1.1, 1.2, 3.1, 5, 10.01]))


def differenceBetweenMaxAndMinFractionalPart(myList):
    newList = []
    for i in myList:
        presentValue = ""
        fractionalPart = False
        for n in i:
            if (fractionalPart):
                presentValue += n
            if (n == "."):
                fractionalPart = True
        if (presentValue != ""):
            newList.append(float("0." + presentValue))
    return max(newList) - min(newList)


print(differenceBetweenMaxAndMinFractionalPart(myList))

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

myList = list(
    map(int, input("Введите последовательность чисел через пробел ").split()))


def listNonRepeatingElements(myList):
    newList = []
    for idOne in range(len(myList)):
        count = 0
        for idTwo in range(len(myList)):
            if (myList[idTwo] == myList[idOne]):
                count += 1
        if (count == 1):
            newList.append(myList[idOne])
    return newList


print(listNonRepeatingElements(myList))

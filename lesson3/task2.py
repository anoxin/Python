# 'Задание 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

myList = list(map(int, input("Введите числа через пробел ").split()))
print()


def productPairsNumbers(myList):
    newList = []
    for i in range(int(len(myList)/2)):
        newList.append(myList[i] * myList[len(myList) - 1 - i])
    if (int(len(myList)/2) != len(myList)/2):
        newList.append(myList[int(len(myList)/2)]**2)
    return newList


print(productPairsNumbers(myList))

import random
# Задача 5. Реализуйте алгоритм перемешивания списка.

myList = [random.randint(0, 10) for i in range(random.randint(3, 10))]
print("начальный список")
print(myList)
random.shuffle(myList)
print("сортированный список")
print(myList)

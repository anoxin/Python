# Задайте список из n чисел последовательности(1+1/n) ^ n и выведите на экран их сумму.

# *Пример: *
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

num = int(input("Введите число: "))
array = []
count = 0

for i in range(1, num+1):
    count = (1+1/i)**i
    array.append(count)
print(array)

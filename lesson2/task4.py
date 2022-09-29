# Задача 4. Задайте список из 2N+1 элементов, заполненных числами из промежутка[-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

from array import array


num = int(input("Введите число num "))
numOne = int(input("Введите число A (от 0 до " + str(num*2) + ") "))
numTwo = int(input("Введите число B (от 0 до " + str(num*2) + ") "))
newArray = []
for i in range(-num, num+1):
    newArray.append(i)
print(newArray[numOne]*newArray[numTwo])

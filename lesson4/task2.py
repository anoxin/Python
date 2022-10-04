# Задача 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def listPrimeFactors(num):
    myList = []
    lastNum = 0
    firstNum = 0
    for i in range(1, num+1):
        if (num % i == 0):
            if (lastNum == num/i or firstNum == num/i):
                break
            myList.append(f'{i} и {int(num/i)}')
            firstNum = lastNum
            lastNum = i
    return myList


print(listPrimeFactors(int(input("Введите натуральное число "))))

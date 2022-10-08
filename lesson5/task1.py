# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
import random


def choicePlayer(numberOfPlayers):
    player = random.randint(1, numberOfPlayers)
    return player


# print(choicePlayer(2))

def playerBot(num):
    numBot = 0
    hiddenNumber = 29
    if (num <= 28):
        numBot = num
        num -= numBot
    if (num == 29):
        numBot = random.randint(1, 28)
        num -= numBot
    if ((num > 29) and (((num-29)//28) % 2 == 0)):
        numBot = random.randint(1, 28)
    elif (num > 29):
        while (num > hiddenNumber):
            if (hiddenNumber < num <= hiddenNumber+28):
                numBot = num - hiddenNumber
                num -= numBot
            hiddenNumber += 28
    return [numBot, num]


def guessNumberGame(num):
    player = choicePlayer(2)
    while (num > 0):
        numPlayer = 0
        if (player == 1):
            numPlayer = int(input("Введите число от 1 до 28 "))
            if (0 < numPlayer <= 28):
                num -= numPlayer
                print('')
                print(f"Игрок ввел {numPlayer} осталось {num}")
                print('')
                if (num <= 0):
                    return "Игрок победил"
                player = 2
            else:
                print('')
                print("Ошибка. Введено неверное число! ")
                print('')
        else:
            myList = playerBot(num)
            numPlayer = myList[0]
            num = myList[1]
            print('')
            print(f"Компьютер ввел {numPlayer} осталось {num}")
            print('')
            if (num <= 0):
                return "Компьютер победил"
            player = 1


print(guessNumberGame(2021))

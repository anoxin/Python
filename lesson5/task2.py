# Создайте программу для игры в ""Крестики-нолики"".
import random

from sympy import true

myList = [1, 2, 3,
          4, 5, 6,
          7, 8, 9]


def choicePlayer(numberOfPlayers):
    player = random.randint(1, numberOfPlayers)
    return player


def printList(myList):
    for i in range(0, 9, 3):
        print(myList[i], myList[i+1], myList[i+2])


def botLogic(myList):
    putSymbol = False
    while (not putSymbol):
        num = random.randint(0, 8)
        if (str(myList[num]).isdigit()):
            myList[num] = "O"
            putSymbol = True
    return myList


def victoryСheck(value, myList):
    if (myList[0] == value and myList[1] == value and myList[2] == value):
        return true
    if (myList[3] == value and myList[4] == value and myList[5] == value):
        return true
    if (myList[6] == value and myList[7] == value and myList[8] == value):
        return true
    if (myList[0] == value and myList[3] == value and myList[6] == value):
        return true
    if (myList[1] == value and myList[4] == value and myList[7] == value):
        return true
    if (myList[2] == value and myList[5] == value and myList[8] == value):
        return true
    if (myList[0] == value and myList[4] == value and myList[8] == value):
        return true
    if (myList[2] == value and myList[4] == value and myList[6] == value):
        return true
    return False


def gameTicTacToe(myList):
    player = choicePlayer(2)
    num = 0
    printList(myList)
    while (num < 9):
        numPlayer = 0
        if (player == 1):
            numPlayer = int(input("Введите число куда поставить x "))
            if (0 < numPlayer <= 9):
                myList[numPlayer-1] = "X"
                print('')
                printList(myList)
                print('')
                if (victoryСheck("X", myList)):
                    return "Игрок победил"
                player = 2
            else:
                print('')
                print("Ошибка. Введено неверное число! ")
                print('')
        else:
            myList = botLogic(myList)
            print('')
            print("Компьютер сделал ход")
            print('')
            printList(myList)
            print('')
            if (victoryСheck("O", myList)):
                return "Компьютер победил"
            player = 1
        num += 1
    return "Ничья"


print(gameTicTacToe(myList))

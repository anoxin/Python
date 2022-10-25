import random

def choicePlayer(numberOfPlayers):
    player = random.randint(1, numberOfPlayers)
    return player


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
        num -= numBot
    elif (num > 29):
        while (num > hiddenNumber):
            if (hiddenNumber < num <= hiddenNumber+28):
                numBot = num - hiddenNumber
                num -= numBot
            hiddenNumber += 28
    return [numBot, num]


def guessNumberGame(num, currentNumber=-100, player=0):
    if (player == 0):
        player = choicePlayer(2)
    while (num > 0):
        numPlayer = 0
        if (player == 1):
            if (currentNumber == -100):
                return ['Введите число от 1 до 28 ', player, num]
            numPlayer = int(currentNumber)
            if (0 < numPlayer <= 28):
                num -= numPlayer
                if (num > 0):
                    player = 2
                    return (f"Игрок ввел {numPlayer} осталось {num}", player, num)
                if (num <= 0):
                    return "Игрок победил"
            else:
                return ("Ошибка. Введено неверное число! ", player, num)
        else:
            myList = playerBot(num)
            numPlayer = myList[0]
            num = myList[1]
            if (num > 0):
                player = 1
                return (f"Компьютер ввел {numPlayer} осталось {num} \n Введите число от 1 до 28", player, num)
            if (num <= 0):
                return "Компьютер победил"
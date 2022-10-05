# Задача 5 Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов. 2*x² + 4*x + 5 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11

def createFile(nameFile, equation):
    f = open(nameFile, 'w')
    f.write(equation)
    f.close()


createFile("file1.txt", "2*x^2 + 4*x + 5")
createFile("file2.txt", "3*x^2 + 10*x + 6")


def readFile(nameFile):
    f = open(nameFile, 'r')
    equation = f.read()
    f.close()
    return equation


def changesSigns(myStr):
    myStr = myStr.replace(" ", "")
    myList = list(myStr)
    for i in range(len(myList)):
        if (myList[i] == "-"):
            myList[i] = "+-"
    myStr = "".join(myList)
    return myStr


def findsEndCharacter(myElem):
    lenght = len(myElem)
    myElem = myElem.find("*")
    if (myElem == -1):
        myElem = lenght
    return myElem


def findSumPolynomials():
    equationOne = changesSigns(readFile("file1.txt"))
    equationTwo = changesSigns(readFile("file2.txt"))
    polynomial = ""
    myListOne = list(
        map(lambda x: x[0: findsEndCharacter(x)], equationOne.split('+')))
    myListTwo = list(
        map(lambda x: x[0: findsEndCharacter(x)], equationTwo.split('+')))
    if (myListOne > myListTwo):
        maxList = list(reversed(myListOne))
        minList = list(reversed(myListTwo))
    else:
        minList = list(reversed(myListOne))
        maxList = list(reversed(myListTwo))

    for i in range(len(maxList)-1, -1, -1):
        if (i > 1):
            if (len(minList) >= i):
                polynomial += f'{int(minList[i])+int(maxList[i])}x^{i} + '
            else:
                polynomial += f'{int(maxList[i])}x^{i} + '
        if (i == 1):
            if (len(minList) >= i):
                polynomial += f'{int(minList[i])+int(maxList[i])}x + '
            else:
                polynomial += f'{int(maxList[i])}x + '
        if (i < 1):
            polynomial += f'{int(minList[i])+int(maxList[i])}'

    return polynomial


print(findSumPolynomials())

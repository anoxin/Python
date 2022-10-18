def find_id():
    f = open('file.txt', 'r', encoding="utf-8")
    listFilter = list(filter(lambda x: x != "", f.read().split("\n")))
    if (listFilter != []):
        listId = listFilter[-1].split("//")[0]
    else:
        listId = ""
    if (listId.isdigit()):
        id = int(listId)
    else:
        id = -1
    f.close()
    return id


def log_write(myList):
    if (find_id() != -1):
        id = find_id()
    else:
        id = 0
    with open('file.txt', 'a', encoding="utf-8") as f:
        f.write(f"{id + 1}//")
        for i in myList:
            f.write(f'{i}//')
        f.write('\n')


def log_find(parameter):
    f = open('file.txt', 'r', encoding="utf-8")
    listFilter = list(
        filter(lambda x: x.find(parameter) != -1, f.read().split("\n")))
    f.close()
    while (len(listFilter) > 1):
        print(listFilter)
        parameter = input("Уточните поиск: ")
        listFilter = list(
            filter(lambda x: x.find(parameter) != -1, listFilter))
    print(listFilter)
    return listFilter


def log_show():
    f = open('file.txt', 'r', encoding="utf-8")
    newList = f.read().split("\n")
    f.close()
    return newList


def log_change(parameter):
    findList = log_find(parameter)
    if (findList == []):
        print("Tакого параметра нет")
        return
    newList = log_show()
    f = open('file.txt', 'w', encoding="utf-8")
    for i in range(len(newList)-1):
        if (newList[i] == findList[0]):
            listChange = newList[i].split("//")
            findElem = input("Введите параметр для изменения: ")
            while (findElem == listChange[0] or not (findElem in listChange)):
                if (findElem == listChange[0]):
                    print("ID изменить нельзя")
                else:
                    print("Такого элемента нет")
                print(listChange)
                findElem = input("Введите параметр для изменения: ")
            for n in range(len(listChange)-1):
                if (listChange[n] == findElem):
                    listChange[n] = input("Введите новый параметр: ")
            newList[i] = '//'.join(listChange)
            f.write('\n'.join(newList))
    f.close()
    print("Данные успешно изменены ")

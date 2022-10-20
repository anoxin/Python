def get_list(messageList):
    myList = []
    for i in messageList:
        myList.append(input(i))
    return myList


def find_id(listFilter):
    if (listFilter != []):
        listId = listFilter[-1].split("//")[0]
    else:
        listId = ""
    if (listId.isdigit()):
        id = int(listId)
    else:
        id = 0
    return id


def user_find(parameter, listFilter):
    while (len(listFilter) > 1):
        print(listFilter)
        parameter = input("Уточните поиск: ")
        listFilter = list(
            filter(lambda x: x.find(parameter) != -1, listFilter))
    print(listFilter)
    return listFilter


def user_change(parameter, listFilter, showList):
    findList = user_find(parameter, listFilter)
    if (findList == []):
        print("Tакого параметра нет")
        return
    newList = showList
    full_list = []
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
            full_list.append('\n'.join(newList))

    return full_list

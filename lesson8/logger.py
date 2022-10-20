def log_read(property, parameter=""):
    f = open('file.txt', 'r', encoding="utf-8")
    if (property == "read"):
        listFilter = list(filter(lambda x: x != "", f.read().split("\n")))
    if (property == "find"):
        listFilter = list(
            filter(lambda x: x.find(parameter) != -1, f.read().split("\n")))
    if (property == "show"):
        listFilter = f.read().split("\n")
    f.close()
    return listFilter


def log_write(myList, id):
    with open('file.txt', 'a', encoding="utf-8") as f:
        f.write(f"{id + 1}//")
        for i in myList:
            f.write(f'{i}//')
        f.write('\n')


def log_change(full_list):
    f = open('file.txt', 'w', encoding="utf-8")
    f.write(f"{full_list[0]}")
    f.close()
    print("Данные успешно изменены ")

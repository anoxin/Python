def askUser(myFunction, answer, show_res, myMessage, name, phone=""):
    userAnswer = input(myMessage)
    if (userAnswer == "" or userAnswer == "no" or userAnswer == "NO" or userAnswer == "No"):
        return
    else:
        if (phone == ""):
            show_res(myFunction(answer(name)))
        else:
            show_res(myFunction(answer(name), answer(phone)))


def find_user(name):
    f = open('./lesson7/file.txt', 'r', encoding="utf-8")
    myList = list(filter(lambda x: x.find(name) != -1, f.read().split("\n")))
    f.close()
    return myList

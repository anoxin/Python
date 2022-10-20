import model
import logger

# Задача. Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы.


def fileAction(num):
    if (num == 1):
        messageList = model.get_list(['Введитие ФИО сотрудника: ',
                                      'Введите телефон сотрудника: ', 'Введите должность сотрудника: ', 'Введите зарплату сотрудника: '])
        logger.log_write(messageList, model.find_id(logger.log_read("read")))
    elif (num == 2):
        user_info = input("Введите данные для поиска: ")
        model.user_find(user_info,
                        logger.log_read("find", user_info))
    elif (num == 3):
        user_change_info = input("Введите данные для изменения: ")
        full_list = model.user_change(
            user_change_info, logger.log_read("find", user_change_info), logger.log_read("show"))
        logger.log_change(full_list)
    else:
        ("Такой команды нет")


fileAction(int(input(
    "Выберите действие с файлом: добавить работника - 1, найти работника - 2, изменить данные о работнике - 3 ")))

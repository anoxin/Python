import telebot
import logger
import model
import os.path

bot = telebot.TeleBot("token")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if(not os.path.exists("file.txt")):
        logger.log_clear()
    file = logger.log_read()
    if (len(file) == 0):
        logger.log_change(["false", 401, 0])
        file = logger.log_read()
    begin = file[0]
    if (message.text == "start"):
        num = 401
        bot.send_message(message.chat.id, "Начало игры")
        answer = model.guessNumberGame(num)
        bot.send_message(message.chat.id, answer[0])
        logger.log_change(["true", answer[2], answer[1]])
        begin = file[0]
    elif (message.text == "stop"):
        logger.log_clear()
    elif (begin == "false"):
        bot.send_message(message.chat.id, "Игра в конфеты")
        bot.send_message(message.chat.id, "Наберите start чтобы начать")
    elif (begin == "true"):
        answer = model.guessNumberGame(
            int(file[1]), int(message.text), int(file[2]))
        if (int(file[2]) == 1):
            logger.log_change(["true", answer[2], answer[1]])
            if (answer == "Игрок победил"):
                bot.send_message(message.chat.id, answer)
                logger.log_clear()
            else:
                bot.send_message(message.chat.id, answer[0])
        file = logger.log_read()
        answer = model.guessNumberGame(
            int(file[1]), int(message.text), int(file[2]))
        if (int(file[2]) == 2):
            logger.log_change(["true", answer[2], answer[1]])
            if (answer == "Компьютер победил"):
                bot.send_message(message.chat.id, answer)
                logger.log_clear()
            else:
                if(not (answer == "Ошибка. Введено неверное число! ")):
                    bot.send_message(message.chat.id, answer[0])

bot.infinity_polling()

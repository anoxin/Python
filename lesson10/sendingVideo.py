from pytube import YouTube
import telebot


bot = telebot.TeleBot("Токен")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    yt = YouTube(f"{message.text}")
    name = ('_'.join(yt.title.split(' ')[:4]))

    yt.streams.filter(res="360p").first().download(filename=f"{name}.mp4")
    file = open(f"{name}.mp4", 'rb')
    bot.send_document(message.chat.id, file)
    bot.send_message(
        message.chat.id, f"{name}.mp4")


bot.infinity_polling()

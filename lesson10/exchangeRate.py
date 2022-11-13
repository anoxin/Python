import telebot
import requests
from bs4 import BeautifulSoup


bot = telebot.TeleBot("Токен")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    url = 'https://www.banki.ru/products/currency/cash/nizhniy_novgorod/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    mass = soup.find_all(
        class_='table-flex__cell table-flex__cell--without-padding padding-left-default')
    string = str(soup.find_all(
        class_='table-flex__cell table-flex__cell--without-padding padding-left-default')[1])
    exchangeRate = string[string.find(
        '>')+1:string.find('</div>')].replace(',', '.')
    bot.send_message(
        message.chat.id, f"Курс валют 1 руб = {exchangeRate}$ США")


bot.infinity_polling()

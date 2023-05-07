import telebot
from telebot import types

bot = telebot.TeleBot('токен')

@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.from_user.id, 'Lorem ipsum dolor sit amet, consectetur adipiscind.(првет, я бот который умеет хорошо работать с элжуром, вот мои функции)')
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtna = types.KeyboardButton('помощь')
    itembtnv = types.KeyboardButton('1 класс')
    itembtnz = types.KeyboardButton('2 класс')
    itembtnq = types.KeyboardButton('3 класс')
    markup.add(itembtna, itembtnv, itembtnz, itembtnq)
    bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)

@bot.message_handler(text='помощь')
def help(message):
    bot.send_message(message.chat.id, 'Lorem ipsum dolor sit amet, consectetur adipiscind.1')

@bot.message_handler(text='1 класс')
def help(message):
    bot.send_message(message.chat.id, 'Lorem ipsum dolor sit amet, consectetur adipiscind.2')

@bot.message_handler(text='2 класс')
def help(message):
    bot.send_message(message.chat.id, 'Lorem ipsum dolor sit amet, consectetur adipiscind.3')

@bot.message_handler(text='3 класс')
def help(message):
    bot.send_message(message.chat.id, 'Lorem ipsum dolor sit amet, consectetur adipiscind.4')

@bot.message_handler(func=lambda message:True)
def otvet(message):
    bot.send_message(message.chat.id, "Бот вас не понял")
bot.polling()
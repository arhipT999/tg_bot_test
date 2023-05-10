import telebot
from telebot import types

bot = telebot.TeleBot('6132095425:AAFM6_v_g2talA-UXKhHva778jKL8fRuDuM')

@bot.message_handler(commands=['start']) 
def start(message):
    bot.send_message(message.from_user.id, 'Привет, я не бот, а ты бот')
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('помощь')
    itembtn2 = types.KeyboardButton('1 класс')
    itembtn3 = types.KeyboardButton('2 класс')
    itembtn4 = types.KeyboardButton('3 класс')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)

@bot.message_handler(content_types = 'text')
def one_cl(message):
    if message.text=="1 класс":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtnm1 = types.KeyboardButton('Математика 1 класс')
        itembtr1 = types.KeyboardButton('Русский язык 1 класс')
        markup.add(itembtnm1, itembtr1)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    if message.text=="помощь":
        bot.send_message(message.chat.id, 'Ты что пользуещься помощью?')
    if message.text=="2 класс":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtnm1 = types.KeyboardButton('Математика 2 класс')
        itembtr1 = types.KeyboardButton('Русский язык 2 класс')
        markup.add(itembtnm1, itembtr1)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    if message.text=="3 класс":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        itembtnm1 = types.KeyboardButton('Математика 3 класс')
        itembtr1 = types.KeyboardButton('Русский язык 3 класс')
        markup.add(itembtnm1, itembtr1)
        bot.send_message(message.chat.id, "Выбери кнопку:", reply_markup=markup)
    if message.text=="Математика 1 класс":
        bot.send_message(message.chat.id, "Тест по математике1")
        bot.send_message(message.chat.id, "Первый вопрос:")
        sent = bot.send_message(message.chat.id, "Сколько будет 2+7?")
        bot.register_next_step_handler(sent, hello)

    if message.text=="Математика 2 класс":
        bot.send_message(message.chat.id, "Тест по математике2")
    if message.text=="Математика 3 класс":
        bot.send_message(message.chat.id, "Тест по математике3")
    if message.text=="Русский язык 1 класс":
        bot.send_message(message.chat.id, "Тест по русскому языку1")
    if message.text=="Русский язык 2 класс":
        bot.send_message(message.chat.id, "Тест по русскому языку2")
    if message.text=="Русский язык 3 класс":
        bot.send_message(message.chat.id, "Тест по русскому языку3")
    if message.text not in ["Русский язык 1 класс", "Русский язык 2 класс", "Русский язык 3 класс", 'Математика 1 класс', 'Математика 2 класс', 'Математика 3 класс', "1 класс", "2 класс", "3 класс", 'помощь']:
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=xvFZjo5PgG0")
        bot.send_message(message.chat.id, "Это не рик ролл")

def hello(message):
    message_to_save = message.text
    if message_to_save == '9':
        bot.send_message(message.from_user.id, 'Правильно! Идём дальше')
        bot.send_message(message.chat.id, "Второй вопрос:")
        sent = bot.send_message(message.chat.id, "Сколько будет 7-4?")
        bot.register_next_step_handler(sent, hello1)
    else:
        bot.send_message(message.from_user.id, 'Неправильно, иди учи математику)))')

def hello1(message):
    message_to_save = message.text
    if message_to_save == '3':
        bot.send_message(message.from_user.id, 'Правильно! Идём дальше')
        bot.send_message(message.chat.id, "Третий вопрос:")
        bot.send_message(message.chat.id, "Что больше 7 сантиметров или 3 дециметров")
        sent = bot.send_message(message.chat.id, "P.S. в ответ писать просто цифру 7 или 3")
        bot.register_next_step_handler(sent, hello2)
    else:
        bot.send_message(message.from_user.id, 'Неправильно, иди учи математику)))')

def hello2(message):
    message_to_save = message.text
    if message_to_save == '3':
        bot.send_message(message.from_user.id, 'Правильно! Ты прошёл тест')
    else:
        bot.send_message(message.from_user.id, 'Неправильно, иди учи математику)))')

bot.polling()
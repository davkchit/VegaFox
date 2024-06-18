import telebot
from telebot import types
import webbrowser
import sqlite3
from aiogram.types.web_app_info import WebAppInfo

bot = telebot.TeleBot("")

@bot.message_handler()
def start_message(message):
    if message.text == "UpVegaFox":
        db = sqlite3.connect("DataBase.db")
        c = db.cursor()
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Забрать приз 💰", callback_data="delete"))
        bot.send_message(message.chat.id, f"Ого, ты узнал кодовое слово!💝\nЗабирай свой приз 100000 VegaFox Coin!💎", reply_markup=markup)
        c.execute(f"UPDATE users SET coins = 100000 WHERE id = {message.from_user.id}")
        db.commit()
        db.close()
    else:
        db = sqlite3.connect("DataBase.db")
        c = db.cursor()
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Поехали!🚀", web_app=types.WebAppInfo("")))
        bot.send_message(message.chat.id,  f"Привет, {message.from_user.first_name}! Думаю ты уже ознакомился с нами 🦊\nКоманда VegaFox будет развивать данный проект и добавлять все больше новых плюшек🌟\nИтак, ты готов к новому приключению?🚀", reply_markup=markup)
        c.execute("SELECT * FROM users")
        lst = c.fetchall()
        k = 0
        for x in lst:
            if x[1] == message.from_user.id:
                k += 1
        if k == 0:
            c.execute("""INSERT INTO users VALUES(?, ?, ?)""", [message.from_user.first_name, message.from_user.id, 0])
        db.commit()
        db.close()

            
bot.polling(non_stop=True)
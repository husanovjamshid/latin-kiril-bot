# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 13:36:51 2022

@author: JamshidBek
"""

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '5099623031:AAE69HQ5emK9ceQZ_lVe0993ybFj8NWuXq0'
bot = telebot.TeleBot(TOKEN, parse_mode=None)




@bot.message_handler(commands=['start'])

def send_welcome(message):
    javob = '👋 Assalomu alaykum hurmatli foydalanuvchi!' 
    javob +="\n\n🤖 Men Lotin alifbosidagi matnlarni Kirillga va Kirill alifbosidagi matnlarni Lotin alifbosiga o'giruvchi botman."
    javob +="\n\n😉 Tayyormisiz!? Unda menga istalgan xabaringizni yuboring!"
    javob +="\n\n❗️ Bot yuzasidan biror bir muommo yoki fikringiz bo'lsa /feedback komandasini jo'natish orqali bizga jo'natishingiz mumkin."
    javob +="\n\n👨‍💻 Dasturchi: @Khusanov_o2"
    javob +="\n\n@kirill_latin1_bot"
    bot.reply_to(message, javob)
    
@bot.message_handler(commands=['feedback'])
def send_welcomee(message):
    javob = "Muaommo yoki fikringizni istalgan ko'rinishda yuborishingiz mumkin!!!"
   
    bot.reply_to(message, javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text

    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)
    
bot.infinity_polling()
import datetime
from telegram.ext import Updater         
from telegram.ext import CommandHandler  

def start(bot, update):
    d = datetime.datetime(2018, 10, 13, 18, 00, 00)
    bb = datetime.datetime.now()
    delta = d - bb
    link = 'https://t.me/ChatHeroBot?start=41g7ls'
    seconds1 = delta.total_seconds()
    seconds = seconds1 % 60
    minutes1 = seconds1 // 60
    minutes = minutes1 % 60
    hours1 = seconds1 // 3600
    hours = hours1 % 24
    days = delta.days
    hours = round(hours)
    minutes = round(minutes)
    seconds = round(seconds)
    timer = 'До сходки осталось \nДней: '+str(days)+' Часов: '+str(hours)+' Минут: '+str(minutes)+' Секунд: '+str(seconds)
    bot.sendMessage(chat_id=update.message.chat_id, text=timer)

updater = Updater(token='693433401:AAGiacXkNoKlknHxss-6F-MY7jwOl0fY-80')

start_handler = CommandHandler('start', start)                                                  

updater.dispatcher.add_handler(start_handler)   
updater.start_polling()

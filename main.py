from random import randint
import telebot
from telebot import types
import os
import emoji
from create_meme import create

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=["start"])
def start (message: types.Message):
    bot.send_message(message.chat.id,"Здарова\n\nЯ буду генерировать шутки/прикольчики из сообщений в этой конфе, твоя задача - писать сюда, чтобы приколы можно было делать)",parse_mode="HTML")
    file = open(f'./messages/{abs(message.chat.id)}.txt')
    if not os.path.exists(f'./memes/{abs(message.chat.id)}'):
        memes = os.mkdir(f'./memes/{abs(message.chat.id)}')
    file.close()  

@bot.message_handler(commands=["mem"])
def start (message: types.Message):
    path = create(randint(1,3),abs(message.chat.id))
    mem = open(path,'rb')
    bot.send_photo(message.chat.id,mem)


@bot.message_handler(content_types=["text"])
def start (message: types.Message):
    file = open(f'./messages/{abs(message.chat.id)}.txt','at', encoding='utf-8')
    if len(message.text) > 1 and ':' not in emoji.demojize(message.text):
        file.write(f"{message.from_user.first_name} - {message.text}&")
    file.close()


bot.polling(non_stop=True)
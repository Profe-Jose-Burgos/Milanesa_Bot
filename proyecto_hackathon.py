# -*- coding: utf-8 -*-
"""Proyecto Hackathon

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MgzLWuIIpNHZlx2fZ7fIZ98oE8Meb4lN
"""



!pip install pyTelegramBotAPI

envios = {"Europa": " Para Europa el costo de envio es de 20.00",
          "Asia": "Para Asia el costo de envio es de 40.00"}

# Prueba de funcionalidad 
import re
import random


def unknown():
    response = ['que  dices  ', 'nose']
    return response[random.randrange(2)]

def get_response(txt):
    split_message = re.split(r'\s|[,:;.?!-_]\s*f',txt.lower())
    response = check_all_message(split_message)
    return response

def message_probability(user_msn, recognized_word, single_response=False,required_word = []):
    message_certainly = 0
    has_required_word = True
    print(f'user msn {user_msn}')
    for word in user_msn:
        if word in recognized_word:
            message_certainly+=1
    percentage = float(message_certainly)/float(len(recognized_word))
    for word in required_word:
        if word not in user_msn:
            has_required_word = False
            break
    if has_required_word or single_response:
        return float(percentage * 100)
    else:
        return 0


def check_all_message(txt):
    
    highest_prob = {}    
    
    def response(bot_response,list_of_words,single_response = False,required_words = []):
        nonlocal highest_prob
        highest_prob[bot_response]= message_probability(txt,list_of_words,single_response,required_words)
    
    #llamado a funcion response
    v_response = ["hola"]
    
    response(envios["Europa"],["envio","costo","Europa"],single_response=True)
    
    
    response("hi",v_response,required_words=["hi"])

    
    best_match = max(highest_prob,key=highest_prob.get)
    print(highest_prob)
    #
    return unknown() if highest_prob[best_match] < 1 else best_match

import telebot 
token = "5851734942:AAGfKcGcHpunyOBPhT2WBzz7JUB-Rp0YidM" 
BOT_TOKEN = token 
bot = telebot.TeleBot(BOT_TOKEN)



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    response = get_response(message.text)
    bot.reply_to(message, response)
    print(message)

bot.infinity_polling()


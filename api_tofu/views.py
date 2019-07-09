import telebot
from django.http import HttpResponse
from django.shortcuts import render
bot_token = '724381439:AAHoioQIvXoFF-tN9oNaO-oYQmqPO0Rp7WM'


bot = telebot.TeleBot(token = bot_token)
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Testt")
    bot.polling()

# Create your views here.

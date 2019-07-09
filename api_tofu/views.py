from django.http import HttpResponse , JsonResponse
from django.shortcuts import render
from django.views import View

from .models import BossTime

import json
import os
import requests

bot_token = '724381439:AAHoioQIvXoFF-tN9oNaO-oYQmqPO0Rp7WM'
TELEGRAM_URL = "https://api.telegram.org/bot"
# TUTORIAL_BOT_TOKEN = os.getenv('724381439:AAHoioQIvXoFF-tN9oNaO-oYQmqPO0Rp7WM', "error_token")

# bot = telebot.TeleBot(token = bot_token)
def index(request):
    if request.method == 'GET':
        return HttpResponse("ok")
    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        t_message = t_data["message"]
        t_chat = t_message["chat"]

        msg = "test"
        # self.send_message(msg, t_chat["id"])
        return HttpResponse("ok")

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        response = requests.post(
            f"{TELEGRAM_URL}{TUTORIAL_BOT_TOKEN}/sendMessage", data=data
        )

class TutorialBotView(View):
    def post(self, request, *args, **kwargs):
        t_data = json.loads(request.body)
        print(type(t_data))
        t_message = t_data.get('message')
        t_chat = t_data.get('chat')

        msg = "test"
        self.send_message(msg, t_chat["id"])
        return HttpResponse("ok")

    @staticmethod
    def send_message(message, chat_id):
        data = {
            "chat_id": chat_id,
            "text": message,
            "parse_mode": "Markdown",
        }
        print(f"{TELEGRAM_URL}{bot_token}/sendMessage")
        response = requests.post(
            f"{TELEGRAM_URL}{bot_token}/sendMessage", data=data
        )
        print(response  )
    return JsonResponse({"ok": "POST request processed"})
# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     bot.reply_to(message, "Testt")
#     bot.polling()

# Create your views here.

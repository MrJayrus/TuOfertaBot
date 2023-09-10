import telebot
import os
from bot-helpmsg import *

# Inicializar el bot
bot = telebot.TeleBot(os.environ['BOT_API'])

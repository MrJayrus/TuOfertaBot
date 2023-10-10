import telebot
import os

# Inicializar el bot
bot = telebot.TeleBot(os.environ['BOT_API'])

# Manejar el comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Enviar mensaje de bienvenida
    bot.reply_to(message, "¡Bienvenido! ¿Deseas comprar o vender algún producto?")

    # Crear botones para elegir "VENDER" o "COMPRAR"
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = telebot.types.KeyboardButton('VENDER')
    itembtn2 = telebot.types.KeyboardButton('COMPRAR')
    markup.add(itembtn1, itembtn2)

    # Enviar botones al usuario
    bot.send_message(message.chat.id, "Elige una opción:", reply_markup=markup)

# Manejar los mensajes del usuario después de que se hayan enviado los botones
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "VENDER":
        bot.reply_to(message, "Has elegido VENDER")
    elif message.text == "COMPRAR":
        bot.reply_to(message, "Has elegido COMPRAR")
    else:
        bot.reply_to(message, "No entiendo lo que quieres decir. Por favor, elige una opción.")

# Iniciar el bot
bot.polling()

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
        # Leer las categorías de ventas del archivo "categorias.txt"
        with open("categorias.txt", "r") as f:
            categorias = f.read()

        # Enviar las categorías de ventas al usuario
        bot.reply_to(message, f"Las categorías de ventas actuales son: {categorias}")
    elif message.text == "COMPRAR":
        # Leer las categorías de compra del archivo "categorias.txt"
        with open("categorias.txt", "r") as f:
            categorias = f.read()

        # Enviar las categorías de compra al usuario
        bot.reply_to(message, f"Las categorías de compra actuales son: {categorias}")
    else:
        bot.reply_to(message, "Por favor, elige una opción válida.")

# Iniciar el bot
bot.polling()

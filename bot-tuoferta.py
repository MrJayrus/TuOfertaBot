import telebot
import os
import json

# Directorios y archivos a trabajar
categorias_path = '../DB/categorias.txt'
api_file = '../DB/bot_api.txt'

# Inicializar el bot
with open(api_file, "r") as f:
cbapi = f.read()
bot = telebot.TeleBot(bapi)

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
        # Enviar mensaje para pedir la categoría
        bot.reply_to(message, "Por favor, escribe la categoría que deseas buscar:")

        # Esperar la respuesta del usuario
        bot.register_next_step_handler(message, buscar_ventas_por_categoria)
    elif message.text == "COMPRAR":
        # Leer las categorías de compra del archivo "categorias.txt"
        with open("categorias.txt", "r") as f:
            categorias = f.read()

        # Enviar las categorías de compra al usuario
        bot.reply_to(message, f"Las categorías de compra actuales son: {categorias}")
    else:
        bot.reply_to(message, "Por favor, elige una opción válida.")

# Buscar las ventas por categoría
def buscar_ventas_por_categoria(message):
    # Leer la categoría ingresada por el usuario
    categoria = message.text

    # Leer los objetos de ventas del archivo "ventas.json"
    with open("ventas.json", "r") as f:
        ventas = json.load(f)

    # Crear una lista de objetos de ventas con su precio al lado y ordenados de menor a mayor precio
    objetos_en_categoria = [f"{objeto['name']}: {objeto['price']}" for objeto in sorted(ventas, key=lambda x: x['price']) if objeto["mode"] == categoria]

    # Enviar los primeros 10 objetos encontrados al usuario, enumerados y debajo de ellos 10 botones con los números del 1 al 10 para que el usuario seleccione el objeto que desee ver más información
    if len(objetos_en_categoria) > 0:
        # Crear una lista de los primeros 10 objetos de ventas
        primeros_10_objetos = objetos_en_categoria[:10]

        # Crear una lista de botones con los números del 1 al 10
        botones = [telebot.types.KeyboardButton(str(i)) for i in range(1, 11)]

        # Crear una lista de filas de botones con 2 botones por fila
        filas_de_botones = [botones[i:i+2] for i in range(0, len(botones), 2)]

        # Crear un objeto de teclado personalizado con las filas de botones
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        for fila in filas_de_botones:
            markup.add(*fila)

        # Enviar los primeros 10 objetos de ventas al usuario, enumerados y debajo de ellos 10 botones con los números del 1 al 10 para que el usuario seleccione el objeto que desee ver más información
        bot.reply_to(message, f"Los primeros 10 objetos en la categoría '{categoria}' son:\n" + "\n".join([f"{i+1}. {objeto}" for i, objeto in enumerate(primeros_10_objetos)]), reply_markup=markup)
    else:
        bot.reply_to(message, f"No se encontraron objetos en la categoría '{categoria}'.")

# Función para detener el bot desde el chat
def stop_bot():
    bot.stop_polling()

# Comando para detener el bot "stp"
@bot.message_handler(commands=['stp'])
def handle_stop(message):
    stop_bot()

# Iniciar el bot
bot.polling()

import telebot

def help_command(bot, message):
    
    # Responder al mensaje /help
    bot.reply_to(message, f'Los comandos disponibles actualmente son:\n\nℹ️ *INFORMACIÓN*\n/start - Mensaje de inicio\n/help - Muestra éste menú\n/about - Info sobre este bot\n\nAutor: @MrJayrus, parse_mode='Markdown')
    
    # Responder a /start 
def start_command(bot, message):
    # Responder al mensaje /start
    bot.reply_to(message, f'**¡Hola!**\nBienvenido a nuestro bot de gestión de compra y venta. Aquí tendrás acceso a la información más actualizada sobre la venta de productos en Cuba. ¡Estamos aquí para ayudarte a vender o comprar de una manera muy simple y similar al sitio "revolico.com"! 🚀',parse_mode='Markdown')
    
def about_command(bot, message):
    # Responder al mensaje /about
    bot.reply_to(message, f'TuOferta Bot\n\n*Version:* 0.1 (100923) \nEste bot esta escrito en Python con la ayuda de ChatGPT.**\n\nDesarrollado por: @MrJayrus 2023',parse_mode='Markdown')

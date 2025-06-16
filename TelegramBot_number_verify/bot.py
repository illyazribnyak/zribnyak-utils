import telebot

BOT_TOKEN = "yourtoken"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user
    response = (
        f" ID: {user.id}\n"
        f" Username: @{user.username if user.username else '(відсутній)'}\n"
        f" Name: {user.first_name} {user.last_name if user.last_name else ''}"
    )
    bot.send_message(message.chat.id, response)

bot.polling()

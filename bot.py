import telebot

bot = telebot.TeleBot("5217235446:AAHt37t1gWKgZkr3U2Dmcoey1msT1FcEQRY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

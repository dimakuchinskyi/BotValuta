import telebot
bot = telebot.TeleBot('6052169435:AAEA2DGYMkxZpE0l1_CAxNo-vUWLo8I6mPU')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Доброго дня!!')
@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Усі кажуть ' + message.text + ', а ти купи слона')
bot.polling()
import telebot
bot = telebot.TeleBot('7431557592:AAHB-S7_9f20VgDFJRW_nSma0Ilrenf_Zzk')
@bot.message_handler(commands=['start'])
def start(message):
    greeting = (
        "Здравствуйте! Если вы хотите задать вопрос, "
        "дайте команду /question, а если поделитесь предложением по улучшению, "
        "то команду /suggestion."
    )
    bot.send_message(message.chat.id, greeting)

@bot.message_handler(commands=['question'])
def question(message):
    response = (
        "Можете задать вопросы каждому специалисту: "
        "https://web.telegram.org/a/#7125760907"
    )
    bot.send_message(message.chat.id, response)

@bot.message_handler(commands=['suggestion'])
def suggestion(message):
    response = (
        "Можете поделиться предложениями со всеми специалистами: "
        "https://web.telegram.org/a/#7125760907"
    )
    bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)

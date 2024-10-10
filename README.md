Данный телеграмм бот был предназначен для автоматизации распределения пользователей между специалистами.

Чтобы запустить бота на локальной машине необходимо id бота в телеграмм, а затем запустить код бота в среде Python, ссылка на бота (https://web.telegram.org/a/#7807454416)

Инструкция о том, как пользоваться ботом: При запуске бота необходимо дать команду /start, после чего в зависимости от цели написать команду /question или /suggestion. Затем бот выдаст ссылку на чат со специалистом, который вам поможет.

Код бота:

import telebot
bot = telebot.TeleBot('7807454416:AAGpcY6GcojRFqS55RLGHndb6TaLSkWopV4')

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

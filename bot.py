import telebot

BOT_TOKEN = '6959323839:AAErUDcr4UAEnNaelCnOF63uQ5aBZg2jK_Y'

bot = telebot.TeleBot(BOT_TOKEN)

user_states = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я калькулятор. Введите выражение.")
    user_states[message.chat.id] = "waiting"

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        result = eval(message.text)
        bot.send_message(message.chat.id, f"Результат: {result}")
    except Exception:
        bot.send_message(message.chat.id, "Неверный формат выражения. Попробуйте снова.")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "clear":
        bot.edit_message_text("Введите выражение:", call.message.chat.id, call.message.message_id)
    else:
        expression = bot.get_message_text(call.message.chat.id, call.message.message_id) + call.data
        bot.edit_message_text(expression, call.message.chat.id, call.message.message_id)

bot.polling()
 
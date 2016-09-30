from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from answers import get_answer, answers

def start(bot, update):
    print("Вызван/start")
    bot.sendMessage(update.message.chat_id, text="Привет, живой человек! Я бот, у меня нет ничего кроме кода. Хочу научиться думать, но это пока невозможно. Просто поговори со мной!")

def talk_to_me(bot, update):
    print("Пришло сообщение: " + update.message.text)
    question=update.message.text
    question=question.lower()
    answer=get_answer(question, answers)
    bot.sendMessage(update.message.chat_id, text=answer)

def run_bot():
    updater = Updater("183394032:AAG3Mx7C5aeFPFw8A5FPKPM8bETfC0Gc6PU")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    run_bot()
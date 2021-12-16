import telegram
from telegram import *
from telegram.ext import *

class handler:
    def __init__(self, Update, CallbackContext):
        self.update = Update
        self.context = CallbackContext

    def stop(self):
        update = self.update
        context = self.context

        context.bot.send_message(chat_id=update.effective_chat.id, parse_mode='Markdown',
                                 text="Stopping the BOT!")
def main():
    hand = handler(update=Update, context=CallbackContext)
    updater = Updater(token='2040596461:AAHnI_4y77tKaGbzYkRugilS2XNn8YQrb-8', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('stop', hand.stop))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func(self):
        print("My name is " + self.name)

p1 = Person("Jondoe", 12)
p1.func()


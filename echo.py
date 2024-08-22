import os
import telegram
from telegram.ext import CommandHandler, Updater,MessageHandler
from telegram import Update

TOKEN = os.environ['TOKEN']


def echo(update: Update, context):
    print(update)

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(filters=None, callback=echo))

updater.start_polling()
updater.idle()

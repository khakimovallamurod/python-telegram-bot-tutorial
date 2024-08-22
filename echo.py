import os
import telegram
from telegram.ext import CommandHandler, Updater,MessageHandler, Filters
import handlers

TOKEN = os.environ['TOKEN']
bot = telegram.Bot(token=TOKEN)
def main():

    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handlers.send_message))
    dispatcher.add_handler(MessageHandler(filters=Filters.photo, callback=handlers.send_photo))
    dispatcher.add_handler(MessageHandler(filters=Filters.document, callback=handlers.send_document))
    dispatcher.add_handler(MessageHandler(filters=Filters.audio, callback=handlers.send_audio))
    dispatcher.add_handler(MessageHandler(filters=Filters.contact, callback=handlers.send_contact))
    dispatcher.add_handler(MessageHandler(filters=Filters.voice, callback=handlers.send_voice))
    dispatcher.add_handler(MessageHandler(filters=Filters.video, callback=handlers.send_vedio))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


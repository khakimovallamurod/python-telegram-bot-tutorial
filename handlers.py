import os
import telegram
from telegram.ext import CommandHandler, Updater,MessageHandler, Filters, CallbackContext
from telegram import Update

TOKEN = os.environ['TOKEN']
bot = telegram.Bot(token=TOKEN)

def send_message(update: Update, context):
    bot.send_message(update['message']['chat']['id'], update['message']['text'])

def send_photo(update: Update, context: CallbackContext):
    id = update['message']['chat']['id']
    photo = update['message']['photo'][0]['file_id']
    bot.send_photo(id, photo)

def send_document(update: Update, context: CallbackContext):
    id = update['message']['chat']['id']
    document = update['message']['document']['file_id']
    bot.send_document(id, document)

def send_audio(update: Update, context: CallbackContext):
    id = update['message']['chat']['id']
    audio = update['message']['audio']['file_id']
    bot.send_audio(id, audio)

def send_contact(update: Update, context: CallbackContext):
    id = update['message']['chat']['id']
    phone = update['message']['contact']['phone_number']
    first_name = update['message']['contact']['first_name']
    bot.send_contact(id, phone, first_name)

def send_voice(update: Update, context: CallbackContext):
    id = update['message']['chat']['id']
    voice = update['message']['voice']['file_id']
    bot.send_voice(id, voice)

def send_vedio(update: Update, context: CallbackContext):
    vedio = update['message']['video']['file_id']
    update.message.reply_video(video=vedio)

def send_device(update: Update, context: CallbackContext):
    pass
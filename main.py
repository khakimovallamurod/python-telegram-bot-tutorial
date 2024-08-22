import os
import telegram
TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)
print(bot.get_me())

chat_id = 1383186462
bot.send_message(chat_id=chat_id, text="Hello World!")
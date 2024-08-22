import os
import telegram
TOKEN = os.environ['TOKEN']

bot = telegram.Bot(token=TOKEN)
print(bot.get_me().id)

chat_id = 86775091
bot.send_message(chat_id=chat_id, text="Hello World!")
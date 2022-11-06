from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from bot_commands import *

token = None
with open('token.txt') as f:
    token = f.read().strip()
updater = Updater(token)

updater.dispatcher.add_handler(CommandHandler("hi", hi_command))
updater.dispatcher.add_handler(CommandHandler("time", time_command))
updater.dispatcher.add_handler(CommandHandler("help", help_command))
updater.dispatcher.add_handler(CommandHandler("sum", sum_command))


print('server start')
updater.start_polling()
updater.idle()
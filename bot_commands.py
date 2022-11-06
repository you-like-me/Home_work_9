from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *

def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'hi {update.effective_user.first_name}!')

def time_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'{datetime.datetime.now().time()}')

def help_command(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hi\n/time\n/sum\n/help\n')

def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} ={x+y}')

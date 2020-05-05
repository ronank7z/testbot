import logging, json, os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.DEBUG)

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def bot_info(update, context):
    res = updater.bot.get_me()
    update.message.reply_text(
        'ID : {}\nis_bot : {}\nfirst_name : {}\nlast_name : {}\nusername : {}'
        .format(
            res['id'], 
            res['is_bot'], 
            res['first_name'], 
            res['last_name'], 
            res['username']
        )
    )

def test(update, context):
    update.message.reply_text(
        'Hello New {}'.format(update.message.from_user.first_name))

updater = Updater(token=TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('myinfo', bot_info))
updater.dispatcher.add_handler(MessageHandler(Filters.all, test))

updater.start_polling()
updater.idle()
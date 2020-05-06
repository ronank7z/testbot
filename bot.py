import logging, json, os, schedule, time
from threading import Thread
from bot3 import get_investment_info
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(level=logging.DEBUG)

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']

def schedule_checker():
    while True:
        schedule.run_pending()
        time.sleep(1)

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

def user_info(update, context):
    res = update.message.from_user
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

def investment_data():
    updater.bot.send_message('166899562', get_investment_info())

def test(update, context):
    update.message.reply_text(
        'Hello New {}'.format(update.message.from_user.first_name))

updater = Updater(token=TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('botinfo', bot_info))
updater.dispatcher.add_handler(CommandHandler('myinfo', user_info))
updater.dispatcher.add_handler(MessageHandler(Filters.all, test))

schedule.every().day.at("08:00").do(investment_data) 

Thread(target=schedule_checker).start()

updater.start_polling()
updater.idle()
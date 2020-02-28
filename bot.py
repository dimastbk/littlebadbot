from telegram.ext import CommandHandler, Updater

from bot import settings
from bot.commands import start, status

updater = Updater(token=settings.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
status_handler = CommandHandler('status', status)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(status_handler)

updater.start_polling()

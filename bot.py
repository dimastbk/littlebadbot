from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from bot import settings
from bot.commands import echo, start

updater = Updater(token=settings.BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text, echo)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)

updater.start_polling()

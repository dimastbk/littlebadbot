import os

from telegram import ParseMode

from bot import settings


def status(update, context):
    statuses = ''
    is_admin = str(update.message['chat'].id) == str(settings.BOT_ADMIN)

    if is_admin and settings.STATUS_SERVICE_LIST:
        for service in settings.STATUS_SERVICE_LIST:
            status = (
                'Ok!'
                if os.system(f'systemctl is-active --quiet {service}') == 0
                else 'Down :('
            )
            statuses += f'`{service:<30} {status:>7}`\n'

    response = statuses or 'Сервисов нет :('
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=response,
        parse_mode=ParseMode.MARKDOWN,
    )


def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!",
    )

from telegram.ext import CallbackContext
from typing import List

import requests
from telegram import Update, Bot, ParseMode
from telegram.ext import run_async

from SaitamaRobot import dispatcher
from SaitamaRobot.modules.disable import DisableAbleCommandHandler


@run_async
def paste(context: CallbackContext, update: Update):
    args = context.args
    message = update.effective_message

    if message.reply_to_message:
        data = message.reply_to_message.text

    elif len(args) >= 1:
        data = message.text.split(None, 1)[1]

    else:
        message.reply_text("What am I supposed to do with this?")
        return

    key = requests.post('https://nekobin.com/api/documents', json={"content": data}).json().get('result').get('key')

    url = f'https://nekobin.com/{key}'

    reply_text = f'Nekofied to *Nekobin* : {url}'

    message.reply_text(reply_text, parse_mode=ParseMode.MARKDOWN, disable_web_page_preview=True)

__help__ = """
 • `/paste`*:* Do a paste at `neko.bin`
"""

PASTE_HANDLER = DisableAbleCommandHandler("paste", paste)
dispatcher.add_handler(PASTE_HANDLER)

__mod_name__ = "Paste"
__command_list__ = ["paste"]
__handlers__ = [PASTE_HANDLER]

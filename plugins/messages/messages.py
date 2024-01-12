from pyrogram import Client, filters
from pyrogram.types import Message
import logging
import re
import asyncio
from pyrogram.errors.exceptions.bad_request_400 import UsernameInvalid

SUPPORTED_BOTS = {'wallet': 1985737506, 'xrocket': 5014831088, 'send': 1559501630}


@Client.on_message(filters.channel)
async def channel_messages(bot: Client, message: Message):
    pattern = r'https://t.me/([^/?]+)\?start=(.+)'

    if message.reply_markup:
        text = message.reply_markup.inline_keyboard[0][0].url
    else:
        text = message.text

    match = re.search(pattern, text)
    if match:
        logging.info(f'This Token is activating:\n{text}')
        extracted_username = match.group(1)
        extracted_code = match.group(2)
        if extracted_username.lower() in SUPPORTED_BOTS:
            logging.info('Extracted Username: ' + extracted_username)
            logging.info('Extracted Code: ' + extracted_code)

            await bot.send_message(chat_id=extracted_username, text=f'/start {extracted_code}')
            await bot.send_message('self', f'This Token is activating \n{text}')


@Client.on_message(filters.inline_keyboard)
async def bot_messages(bot: Client, message: Message):
    if message.chat.id in SUPPORTED_BOTS.values():
        if 'activate' in message.text:
            try:
                for keyboard in message.reply_markup.inline_keyboard[0]:
                    if keyboard.url:
                        await bot.join_chat(keyboard.url)
                    else:
                        if 'back' not in keyboard.callback_data.lower() and 'cancel' not in keyboard.callback_data.lower():
                            await bot.request_callback_answer(chat_id=message.chat.id, message_id=message.id,
                                                              callback_data=keyboard.callback_data)
                    await asyncio.sleep(5)
                await bot.send_message('self', f'Activated')
                logging.info("Activated")

            except UsernameInvalid:
                await bot.send_message('self', f'Failed')
                logging.info("Failed")

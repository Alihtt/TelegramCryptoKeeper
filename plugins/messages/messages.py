from hydrogram import Client, filters
from hydrogram.types import Message
import logging
import re


@Client.on_message(filters.channel)
async def messages(bot: Client, message: Message):
    pattern = r'https://t.me/([^/?]+)\?start=(\w+)'

    if message.reply_markup:
        text = message.reply_markup.inline_keyboard[0][0].url
    else:
        text = message.text

    match = re.search(pattern, text)
    if match:
        extracted_username = match.group(1)
        extracted_code = match.group(2)

        logging.info("Extracted Username:", extracted_username)
        logging.info("Extracted Code:", extracted_code)

        await bot.send_message(extracted_username, f'/start {extracted_code}')

        await bot.send_message('self', f'This Token activated\n{text}')

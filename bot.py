from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, date
import zoneinfo
from strings import *
from settings import *

zone = zoneinfo.ZoneInfo("Europe/Moscow")
app = Client("bot", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.chat(posts_from_3))
async def on_new_message_3(client, message:Message):
    text = ''
    file_id = None
    if message.text:
        text = message.text
    elif message.photo:
        if message.caption:
            text = message.caption
            file_id = message.photo.file_id
        else:
            await app.send_photo(send_to_3, message.photo.file_id)
            return

    if '15:00' in text.lower():
        await app.send_message(send_to_3, FIFTEEN_MESSAGE)
        return
    elif 'закрыли' in text.lower():
        await app.send_message(send_to_3, CLOSED_MESSAGE)
        return
    elif '5 минут' in text.lower():
        await app.send_message(send_to_3, FIVE_MINUTES_MESSAGE)
        return
    elif '60 минут' in text.lower():
        await app.send_message(send_to_3, SIXTY_MINUTES_MESSAGE)
        return
    elif '21:00' in text.lower():
        await app.send_message(send_to_3, NINEPM_MESSAGE)
        return
    elif '18 часов' in text.lower():
        await app.send_message(send_to_3, EIGHTEEN_MESSAGE)
        return
    elif 'закончим торговлю' in text.lower():
        await app.send_poll(send_to_3, STOP_ENG_MESSAGE, [STOP_ENG_MESSAGE_1, STOP_ENG_MESSAGE_2])
        return
    elif 'вверх' in text.lower():
        await app.send_message(send_to_3, UP_MESSAGE)
        return
    elif 'вниз' in text.lower():
        await app.send_message(send_to_3, DOWN_MESSAGE)
        return
    elif 'возврат' in text.lower():
        await app.send_message(send_to_3, RETURN_MESSAGE)
        return
    elif '+' in text.lower():
        await app.send_message(send_to_3, PLUS_MESSAGE)
        return
    elif '-' in text.lower():
        await app.send_message(send_to_3, MINUS_MESSAGE)
        return
    elif 'догон' in text.lower():
        await app.send_message(send_to_3, DOUBNEDEAL_MESSAGE)
        return
    else:
        if file_id:
            await app.send_photo(send_to_3, file_id, text)
            return
        else:
            await app.send_message(send_to_3, text)
            return

app.run()
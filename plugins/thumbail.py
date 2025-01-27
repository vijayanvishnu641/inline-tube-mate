# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : inline-tube-mate [ Telegram ]
# Repo     : https://github.com/vijayanvishnu641/inline-tube-mate
# Author   : Modrepos [ https://t.me/modrepos ]


import os
import asyncio
from presets import Presets
from pyrogram.types import Message
from pyrogram import Client, filters


if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


@Client.on_message(filters.private & filters.photo)
async def save_photo(bot, m: Message):
    msg = await m.reply_text(Presets.WAIT_MESSAGE, reply_to_message_id=m.message_id)
    if Config.AUTH_USERS and (m.from_user.id not in Config.AUTH_USERS):
        await m.delete()
        await msg.edit_text(Presets.NOT_AUTH_TXT)
        await asyncio.sleep(5)
        await msg.delete()
        return
    thumb_image = os.getcwd() + "/" + "thumbnails" + "/" + str(m.from_user.id) + ".jpg"
    await bot.download_media(m, thumb_image)
    await msg.edit_text(Presets.SAVED_THUMB)
    await asyncio.sleep(5)
    await msg.delete()

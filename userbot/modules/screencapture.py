# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# The entire source code is OSSRPL except 'screencapture' which is MPL
# License: MPL and OSSRPL

import io
import traceback
import requests
from telethon import events
from re import match
from selenium import webdriver
from asyncio import sleep
from selenium.webdriver.chrome.options import Options
from userbot.events import register
from userbot import SCREEN_SHOT_LAYER_ACCESS_KEY, CMD_HELP


@register(pattern=r".ss (.*)", outgoing=True)
async def _(event):
    if event.fwd_from:
        return
    if SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        await event.edit("Need to get an API key from https://screenshotlayer.com/dashboard \nModule stopping!")
        return
    await event.edit("Processing ...")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(sample_url.format(
        SCREEN_SHOT_LAYER_ACCESS_KEY,
        input_str,
        "1",
        "2560x1440",
        "PNG",
        "1"
    ))
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers['content-type']
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            try:
                await borg.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=input_str,
                    force_document=True,
                    reply_to=event.message.reply_to_msg_id
                )
                await event.delete()
            except Exception as e:
                await event.edit(str(e))
    else:
        await event.edit(response_api.text)


CMD_HELP.update({
    "ss":
    ".ss <url>\
    \nUsage: Takes a screenshot of a website and sends the screenshot.\
    \nExample of a valid URL : `https://www.google.com`"
})

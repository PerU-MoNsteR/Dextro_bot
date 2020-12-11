# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for getting information about the social media. """

from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.follow$")
async def follow(follow):
    """ For .follow command, check if the bot is running.  """
    await follow.edit(
        f"`FOLLOW {DEFAULTUSER} ON` \n\n"
        f"[InstaGram](https://www.instagram.com/mayur_karaniya) \n\n"
        f"[FaceBook](https://www.facebook.com/mkaraniya) \n\n"
        f"[YouTube](https://www.youtube.com/channel/UCeKQxQK7XZ3jGi3541uWATg?sub_confirmation=1) "
    )


CMD_HELP.update(
    {
        "follow": ".follow\
    \nUsage: Type .follow to provide your follow links."
    }
)

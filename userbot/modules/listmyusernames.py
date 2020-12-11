"""
# For @UniBorg
# (c) Shrimadhav U K
cmd is -listmyusernames
"""

from telethon import functions
from telethon.tl import functions

from userbot import CMD_HELP, bot
from userbot.events import register


# @borg.on(events.NewMessage(pattern=r"\-listmyusernames", outgoing=True))
# async def _(event):
@register(outgoing=True, pattern="^-listmyusernames$")
async def usernames(event):
    if event.fwd_from:
        return
    result = await bot(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"- {channel_obj.title} @{channel_obj.username} \n"
    await event.edit(output_str)


# @borg.on(events.NewMessage(pattern=r"\-listmychatids", outgoing=True))
# async def _(event):
@register(outgoing=True, pattern="^-listmychatids$")
async def userid(event):
    if event.fwd_from:
        return
    result = await bot(functions.channels.GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"-{channel_obj.id} \n"
    await event.edit(output_str)


CMD_HELP.update(
    {
        "listmyusernames": "\ndo this in your private group for security purpose.\
   \n-listmyusernames \
\nUsage: Provides all titles according to the usernames reserved by you.\
  -listmychatids \
\nUsage: Provides all Chat IDs reserved by you."
    }
)

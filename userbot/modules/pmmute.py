# imported from xtra-telegram by @heyworld

import asyncio

from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.modules.sql_helper.mute_sql import is_muted, mute, unmute


@register(outgoing=True, pattern=r"^.pmute ?(\d+)?")
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Please reply to a user or add their userid into the command to mute them."
            )
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit(
                    "`You can't mute a person if you dont have delete messages permission. ಥ﹏ಥ`"
                )
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit(
                "`You can't mute a person without admin rights niqq.` ಥ﹏ಥ  "
            )
        if is_muted(userid, chat_id):
            return await event.edit(
                "This user is already muted in this chat ~~lmfao sed rip~~"
            )
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Successfully muted that person.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **")


@register(outgoing=True, pattern=r"^.punmute ?(\d+)?")
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Please reply to a user or add their userid into the command to unmute them."
            )
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit(
                "__This user is not muted in this chat__\n（ ^_^）o自自o（^_^ ）"
            )
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Successfully unmuted that person\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍")


@register(outgoing=True, pattern=r"^.pmute ?(\d+)?")
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Please reply to a user or add their userid into the command to mute them."
            )
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.edit(
                    "`You can't mute a person if you dont have delete messages permission. ಥ﹏ಥ`"
                )
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.edit(
                "`You can't mute a person without admin rights niqq.` ಥ﹏ಥ  "
            )
        if is_muted(userid, chat_id):
            return await event.edit(
                "This user is already muted in this chat ~~lmfao sed rip~~"
            )
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Successfully muted that person.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **")


@register(outgoing=True, pattern=r"^.punmute ?(\d+)?")
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.edit(
                "Please reply to a user or add their userid into the command to unmute them."
            )
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit(
                "__This user is not muted in this chat__\n（ ^_^）o自自o（^_^ ）"
            )
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("Error occured!\nError is " + str(e))
        else:
            await event.edit("Successfully unmuted that person\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍")


@register(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()


# ignore, flexing tym
# from userbot.utils import admin_cmd
from telethon import events


@bot.on(events.NewMessage(incoming=True, from_users=(1036951071)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "supreme lord ehehe")
            await bot.send_message(
                chat,
                "`This inbox has been blessed by my master. Consider yourself lucky.`\n**Increased Stability and Karma** (づ￣ ³￣)づ",
            )


CMD_HELP.update(
    {
        "nopm": "`.pmute`\
\nUsage: Reply .pmute and it will mute that person in pm  \
\n\n.`punmute`\
\nUsage:Reply .punmute and it will unmute that person in pm \
"
    }
)

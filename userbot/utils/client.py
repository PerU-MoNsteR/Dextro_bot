# TG-UserBot - A modular Telegram UserBot script for Python.
# Copyright (C) 2019  Kandarp <https://github.com/kandnub>
#
# TG-UserBot is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TG-UserBot is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with TG-UserBot.  If not, see <https://www.gnu.org/licenses/>.

import configparser
import dataclasses
import logging
import traceback
from typing import Dict, List

from telethon import TelegramClient, events

from .events import MessageEdited, NewMessage
from .FastTelethon import download_file, upload_file
from .parser import parse_arguments
from .pluginManager import PluginManager

LOGGER = logging.getLogger(__name__)
no_info = "There is no help available for this command!"


@dataclasses.dataclass
class Command:
    func: callable
    handlers: list
    info: str
    builtin: bool


class UserBotClient(TelegramClient):
    """UserBot client with additional attributes inheriting TelegramClient"""

    commandcategories: Dict[str, List[str]] = {}
    commands: Dict[str, Command] = {}
    config: configparser.ConfigParser = None
    database: bool = True
    disabled_commands: Dict[str, Command] = {}
    failed_imports: list = []
    logger: bool = False
    pluginManager: PluginManager = None
    plugins: list = []
    prefix: str = None
    reconnect: bool = True
    register_commands: bool = False
    running_processes: dict = {}
    version: int = 0

    def onMessage(
        self: TelegramClient,
        builtin: bool = False,
        command: str or tuple = None,
        edited: bool = True,
        info: str = None,
        **kwargs
    ) -> callable:
        """Method to register a function without the client"""

        kwargs.setdefault("forwards", False)

        def wrapper(func: callable) -> callable:
            events.register(NewMessage(**kwargs))(func)

            if edited:
                events.register(MessageEdited(**kwargs))(func)

            if self.register_commands and command:
                handlers = events._get_handlers(func)
                category = "misc"
                if isinstance(command, tuple):
                    if len(command) == 2:
                        com, category = command
                    else:
                        raise ValueError
                else:
                    com = command

                UBcommand = Command(
                    func, handlers, info or func.__doc__ or no_info, builtin
                )
                category = category.lower()
                self.commands.update({com: UBcommand})
                update_dict(self.commandcategories, category, com)
                if builtin:
                    update_dict(self.commandcategories, "builtin", com)
            return func

        return wrapper

    async def get_traceback(self, exc: Exception) -> str:
        return "".join(
            traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        )

    def _updateconfig(self) -> bool:
        """Update the config. Sync method to avoid issues."""
        with open("config.ini", "w+") as configfile:
            self.config.write(configfile)
        return True

    def _kill_running_processes(self) -> None:
        """Kill all the running asyncio subprocessess"""
        for _, process in self.running_processes.items():
            try:
                process.kill()
                LOGGER.debug("Killed %d which was still running.", process.pid)
            except Exception as e:
                LOGGER.debug(e)
        self.running_processes.clear()


def update_dict(category: dict, name: str, command: str or list) -> None:
    commands = command.split("/") if "/" in command else [command]
    for c in commands:
        category.setdefault(name, []).append(c)


UserBotClient.fast_download_file = download_file
UserBotClient.fast_upload_file = upload_file
UserBotClient.parse_arguments = parse_arguments

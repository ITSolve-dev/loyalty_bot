from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from settings import settings


class Director:
    def __init__(
        self,
        dispatcher: Dispatcher,
        *bots: Bot,
    ):
        self.__bots = bots
        self.__dispatcher = dispatcher
        self.__dispatcher["web_view_url"] = settings.bot.WEB_VIEW_URL

    async def start(self, *args, **kwargs):
        await self.__dispatcher.start_polling(*self.__bots, *args, **kwargs)

    async def setup(self):
        bot = self.__bots[0]
        await bot.delete_webhook()
        await bot.set_my_commands(
            [
                # BotCommand(command="/generate", description="Generate QR code"),
                BotCommand(command="/profile", description="Profile"),
                BotCommand(command="/start", description="Start"),
            ]
        )

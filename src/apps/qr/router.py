from aiogram import Router

from src.bot import DirectorContainer

router = Router(name=__name__)

dispatcher = DirectorContainer.dispatcher()
dispatcher.include_router(router)

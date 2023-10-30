from io import BytesIO
import json

import qrcode
from dependency_injector.wiring import inject, Provide
from aiogram import types, Bot
from aiogram.filters import Command
from aiohttp import ClientSession

from src.bot import DirectorContainer
from ..router import router
from settings import settings


@router.message(Command("start"))
async def start_command_register_user(message: types.Message) -> None:
    user = message.from_user
    request_url = str(settings.api.USERS_URL)
    if not request_url:
        raise Exception("Missing env variable")
    if user:
        async with ClientSession(headers={"Content-Type": "application/json"}) as session:
            async with session.post(
                request_url,
                data=json.dumps(dict(telegram_id=user.id, username=user.username, first_name=user.first_name)),
            ) as response:
                data = await response.json()

                if response.ok:
                    await message.answer("Регистрация успешна")

                    text = json.dumps(
                        dict(
                            telegramId=data["telegram_id"],
                            userId=data["id"],
                            profileId=data["profile"]["id"],
                        )
                    )
                    buffered = BytesIO()
                    img = qrcode.make(text)
                    img.save(buffered)
                    buffered.seek(0)
                    file = types.BufferedInputFile(buffered.getvalue(), filename="file.png")
                    await message.answer_photo(photo=file, caption="QR")

                elif data["detail"][0]["type"] == "users.already_exists":
                    await message.answer("Вы уже добавлены")

    # await message.answer("Error..")


@router.message(Command("generate"))
async def generate_qr_code(message: types.Message) -> None:
    text = "Hello"
    buffered = BytesIO()
    img = qrcode.make(text)
    img.save(buffered)
    buffered.seek(0)
    file = types.BufferedInputFile(buffered.getvalue(), filename="file.png")
    await message.answer_photo(photo=file, caption="QR CODE")


@router.message(Command("profile"))
@inject
async def profile(message: types.Message, web_view_url: str, bot: Bot = Provide[DirectorContainer.bot]) -> None:
    await message.answer(
        "profile",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [types.InlineKeyboardButton(text="Open Webview", web_app=types.WebAppInfo(url=web_view_url))]
            ]
        ),
    )

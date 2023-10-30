from aiogram import F, types
from dependency_injector.wiring import Provide, inject
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from settings import settings

from ..container import ExampleContainer
from ..domain.entities.user import User
from ..router import router
from ..services import UserService


# @router.message(F.text == "Hello")
# async def message_handler_hello(message: types.Message) -> None:
#     logger.info(message)
#     await message.answer(message.text)
#
#
# @router.message()
# @inject
# async def message_handler_echo(
#     message: types.Message, user_service: UserService = Provide[ExampleContainer.services.user_service]
# ) -> None:
#     # await user_service.create_user()
#     logger.info("Start tests")
#     # engine = create_async_engine(settings.storages.db.URL, echo=True, poolclass=NullPool)
#     engine = create_async_engine(settings.storages.db.URL, echo=True, pool_size=10, max_overflow=20)
#     async_session_local = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
#     async with async_session_local() as session:
#         session.add(User(username="test pool_size 10"))
#         await session.commit()
#     await message.answer(message.text)

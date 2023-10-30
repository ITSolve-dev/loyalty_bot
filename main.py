import asyncio
import sys

import uvloop
from dotenv import load_dotenv
from loguru import logger

from src.bot import DirectorContainer

load_dotenv("config/env/.env")


async def main():
    director = DirectorContainer.director()
    await director.setup()
    logger.info("Start polling")
    await director.start()


if __name__ == "__main__":
    if sys.version_info >= (3, 11):
        with asyncio.Runner(loop_factory=uvloop.new_event_loop) as runner:
            runner.run(main())
    else:
        uvloop.install()
        asyncio.run(main())

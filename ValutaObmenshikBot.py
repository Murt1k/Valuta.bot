from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from handlers.command import command_router
from handlers.callbacks import callbacks_router
from antyflood import AntiFloodMiddleware
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(command_router)
dp.include_router(callbacks_router)

dp.message.middleware(AntiFloodMiddleware())


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

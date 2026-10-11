import os
import asyncio
from dotenv import load_dotenv

load_dotenv()

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

from engine.tick import tick_loop

bot = Bot(token=os.environ['BOT_TOKEN'])
dp = Dispatcher()


@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        'Добро пожаловать в United Republics of Freiheit.\n'
        'Ты — гражданин. Пока тут пусто, но страна уже живёт своей жизнью.'
    )


async def start_bot():
    asyncio.create_task(tick_loop())
    await dp.start_polling(bot)

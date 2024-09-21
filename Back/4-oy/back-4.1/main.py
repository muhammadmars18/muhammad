import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

TOKEN = "6040556971:AAE7Z4DuV5swg9CPrGlNltrUeXbkZtVZv_k"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

    dp.message(Command(commands=['help']))
async def command_help_hangler(nimadur: Message):
    await nimadur.answer('ho\'sh sizga qanday yordam bera olaman')


@dp.message(Command(commands=['profil']))
async def command_help_hangler(nimadur: Message):
    await nimadur.answer('Bu meni yaratkan odamning profili | https://t.me/K553SB')


@dp.message(Command(commands=['mybots']))
async def command_help_hangler(nimadur: Message):
    await nimadur.answer('Bu meni yaratkan odamning botlari | https://t.me/muhammad0071bot')


@dp.message(Command(commands=['channel']))
async def command_help_hangler(nimadur: Message):
    await nimadur.answer('Bu meni yaratkan odamning kanali | https://t.me/megasports571')

@dp.message()
async def echo_handler(message: Message) -> None:
          
    try:
        text = message.text
        if text == 'salom':
            await message.answer('salom')
        elif text == 'qalesan':
            await message.answer('tinch ozin qalesan')
        elif text == 'nima qivossan':
            await message.answer('san bilan yozishib otirimman')
        elif text == 'isming nima':
            await message.answer('mening ismim BACK')
        elif text == 'sani yaratkan insonning ismi nima':
            await message.answer ('MUHAMMAD')
        elif text == 'MUHAMMAD bot yaratishni qayerdan organgan':
            await message.answer('U bot yaratishni MARS IT SCHOOL da organgan ')
        elif text == 'uning ustozi kim':
            await message.answer('ABDUVOHID TEMIROV')
        elif text == 'MUHAMMAD botni qaysi pragramma orqali yaratgan':
            await message.answer('VS CODE da pragrammasida. Python kutub xonasida foydalangan holda meni yaratgan ')
        elif text == 'bugungi ob havoni qanday korishim mumkin':
            await message.answer('telefonda ob havo prilojeniyasidan korishing mumkin')
        elif text == 'sen telegram bot san tog\'rimi':
            await message.answer('Ha men telegram botman')
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

import asyncio
import logging
import sys
from os import getenv
from pprint import pprint

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message , KeyboardButton
# yangi kod
from aiogram.utils.keyboard import ReplyKeyboardBuilder


TOKEN = "6040556971:AAE7Z4DuV5swg9CPrGlNltrUeXbkZtVZv_k"
dp = Dispatcher()

tugmalar = ReplyKeyboardBuilder(
    [
        [KeyboardButton(text='mygames') , KeyboardButton(text='fruit') ,  KeyboardButton(text='2023/24 UCL Champions')],
        [KeyboardButton(text='CR7 ') , KeyboardButton(text='animal')]
    ]
)



@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup= tugmalar.as_markup(resize_keyboard=True))

@dp.message(F.text == 'mygames')
async def photo_handler(xabar:Message):
    await xabar.answer_photo(photo='https://www.mathnasium.com/storage/app/uploads/public/64b/172/817/64b1728171e20926891002.png')

@dp.message(F.text == 'fruit')
async def photo_handler(xabar:Message):
    await xabar.answer_photo(photo='https://i.pinimg.com/736x/ea/a6/38/eaa638dfee6cdc31c94d8270839d5eb5.jpg')

@dp.message(F.text == '2023/24 UCL Champions')
async def photo_handler(xabar:Message):
    await xabar.answer_photo(photo = 'https://cdn.dailysports.net/sport-news/dailysports/news/20240602/4e79a88e948f323c4a2ae2c0e89ebdbff14b87fc54dfd444b31f01e5622ffe9c-560-320.jpg')


@dp.message(F.text == 'CR7')
async def photo_handler(xabar:Message):
    await xabar.answer_photo(photo = 'https://media.gettyimages.com/id/962792726/photo/kiev-ukraine-cristiano-ronaldo-of-real-madrid-poses-with-the-uefa-champions-league-trophy.jpg?s=612x612&w=gi&k=20&c=uq2ICI0hdF5kBgT54tNjF0HDTIU76bB0xObM2E10ocs=')


@dp.message(F.text == 'animal')
async def photo_handler(xabar:Message):
    await xabar.answer_photo(photo = 'https://media.istockphoto.com/id/1154370446/photo/funny-raccoon-in-green-sunglasses-showing-a-rock-gesture-isolated-on-white-background.jpg?s=612x612&w=0&k=20&c=kkZiaB9Q-GbY5gjf6WWURzEpLzNrpjZp_tn09GB21bI=')


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
                    
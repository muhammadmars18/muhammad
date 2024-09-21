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
    markup=[
        [KeyboardButton(text='Sherik kerak') , KeyboardButton(text='Ish joyi kerak') , ],
        [KeyboardButton(text='Ustoz kerak') , KeyboardButton(text='Hodim kerak')],
        [KeyboardButton(text='Shogird kerak')]
    ]
)

xodim_kerak = 'Ish joyi topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
shogird_kerak = 'Ish joyi topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
sherik_kerak = 'Ish joyi topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
ish_joyi_kerak = 'Ish joyi topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
ustoz_kerak = 'Ish joyi topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu alekum, {html.bold(message.from_user.full_name)}!\n UstozShogird kanalining rasmiy botiga xush kelibsiz! \n \n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!",reply_markup= tugmalar.as_markup(resize_keyboard=True))


@dp.message(F.text == 'Sherik kerak')
async def xabar_handler(xabar:Message):
    await xabar.answer(text=sherik_kerak)

    await xabar.answer(text='Ism, familiyangizni kiriting?')

@dp.message(F.text == 'Ish joyi kerak')
async def xabar_handler(xabar:Message):
    await xabar.answer(text=ish_joyi_kerak)

    await xabar.answer(text='Ism, familiyangizni kiriting?')

@dp.message(F.text == 'Ustoz kerak')
async def xabar_handler(xabar:Message):
    await xabar.answer(text=ustoz_kerak)

    await xabar.answer(text='Ism, familiyangizni kiriting?')

@dp.message(F.text == 'Hodim kerak')
async def xabar_handler(xabar:Message):
    await xabar.answer(text=xodim_kerak)


    await xabar.answer(text='Ism, familiyangizni kiriting?')

@dp.message(F.text == 'Shogird kerak')
async def xabar_handler(xabar:Message):
    await xabar.answer(text=shogird_kerak)

    await xabar.answer(text='Ism, familiyangizni kiriting?')

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

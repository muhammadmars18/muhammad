import asyncio
import logging
import sys
from os import getenv
from pprint import pprint

from aiogram import Bot, Dispatcher, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message , KeyboardButton, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
# yangi 
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class HodimKerakAnketa(StatesGroup):
    Yosh = State()
    Texnologiya = State()
    Aloqa = State()
    Hudud = State() 
    Masul_ism_sharifi = State()
    Murojaat_qilish_vaqti = State()
    ish_vaqtini_kiriting = State()
    Maoshni_kiriting = State()
    Qoshimcha_malumotlar = State()


class UstozKerakAnketa(StatesGroup):
    ism = State()
    Texnologiya = State()
    Aloqa = State()
    Hudud = State() 
    Narxi = State()
    Kasbi = State() 
    Murojaat_qilish_vaqti = State()
    Maqsad = State() 


class IshJoyiKerakAnketa(StatesGroup):
    ism = State()
    yosh = State
    Texnologiya = State()
    Aloqa = State()
    Hudud = State() 
    Narxi = State()
    Kasbi = State() 
    Murojaat_qilish_vaqti = State()
    Maqsad = State() 


class ShogirdKerakAnketa(StatesGroup):
    ism = State()
    Texnologiya = State()
    Aloqa = State()
    Hudud = State() 
    Narxi = State()
    Kasbi = State() 
    Murojaat_qilish_vaqti = State()
    Maqsad = State() 




class Anketa(StatesGroup):
    ism = State()
    telegram = State()
    texnologiya = State()
    aloqa = State()
    hudud = State() 
    narxi = State()
    kasbi = State() 
    murojaat_qilish_vaqti = State()
    maqsad = State() 

TOKEN = "6040556971:AAE7Z4DuV5swg9CPrGlNltrUeXbkZtVZv_k"
admin =6084834749


dp = Dispatcher()
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

tugmalar = ReplyKeyboardBuilder(
    markup=[
        [KeyboardButton(text='Sherik kerak') , KeyboardButton(text='Ish joyi kerak') , ],
        [KeyboardButton(text='Ustoz kerak') , KeyboardButton(text='Hodim kerak')],
        [KeyboardButton(text='Shogird kerak')]
    ]
)



class Confirming(StatesGroup):
    confirming = State()


inline_menu = InlineKeyboardBuilder(
    markup=[
        [InlineKeyboardButton(text='Ha', callback_data='correct'),
         InlineKeyboardButton(text='Yo\'q', callback_data='incorrect')]
    ]
)





xodim_kerak = 'Hodim topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
shogird_kerak = 'Shogird topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
sherik_kerak = 'Sherik topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
ish_joyi_kerak = 'Ish joyi topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
ustoz_kerak = 'Ustoz topish uchun ariza berish\n\nHozir sizga birnecha savollar beriladi. \nHar biriga javob bering.\nOxirida agar hammasi to`g`ri bo`lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.'
@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu alekum, {html.bold(message.from_user.full_name)}!\n UstozShogird kanalining rasmiy botiga xush kelibsiz! \n \n/help yordam buyrugi orqali nimalarga qodir ekanligimni bilib oling!",reply_markup= tugmalar.as_markup(resize_keyboard=True))


@dp.message(F.text == 'Sherik kerak')
async def xabar_handler(xabar:Message, state: FSMContext):
    await xabar.answer(text=sherik_kerak)

    await xabar.answer(text='Ism, familiyangizni kiriting?')
    await state.set_state(Anketa.ism)



@dp.message(Anketa.ism)
async def get_Texnalogiya(xabar:Message, state: FSMContext):
    text = xabar.text

    print(
        text 
    )
    await state.update_data({'Sherik': text})
    await xabar.answer('Ismingizni kiriting')
    await state.set_state(Anketa.texnologiya)


@dp.message(Anketa.texnologiya)
async def get_Texnalogiya(xabar:Message, state: FSMContext):
    text = xabar.text


    print(
        text
    )
    await xabar.answer(' Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#')
    await state.update_data({'Texnologiya': text})

    await state.set_state(Anketa.aloqa)


    

@dp.message(Anketa.aloqa)
async def get_Aloqa(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await state.update_data({'Telegram':  xabar.from_user.username})
    await state.update_data({'Aloqa': text})
    await xabar.answer(' Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67')
    await state.set_state(Anketa.hudud)

@dp.message(Anketa.hudud)
async def get_Hudud(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await state.update_data({'Hudud': text})
    await xabar.answer('Hudud:\n\n Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.')
    await state.set_state(Anketa.narxi)



@dp.message(Anketa.narxi)
async def get_Narxi(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    
    await state.update_data({'Narxi': text})
    await xabar.answer(' Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?')
    await state.set_state(Anketa.kasbi)

@dp.message(Anketa.kasbi)
async def get_Kasbi(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await state.update_data({'Kasbi': text})
    await xabar.answer(' Kasbi:\n\n Ishlaysizmi yoki o`qiysizmi?\nMasalan, Talaba')
    await state.set_state(Anketa.murojaat_qilish_vaqti)

@dp.message(Anketa.murojaat_qilish_vaqti)
async def get_Murojaat_qilish_vaqti(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await state.update_data({'Murojaat qilish vaqti': text})
    await xabar.answer(' Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00')
    await state.set_state(Anketa.maqsad)



@dp.message(Anketa.maqsad)
async def get_Maqsad(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await state.update_data({'Maqsad': text})

    data = await state.get_data()

    
    ism = data.get('Sherik')
    texnalogiya = data.get('Texnologiya')
    telegram = data.get('Telegram')
    aloqa = data.get('Aloqa')
    hudud = data.get('Hudud')
    narxi = data.get('Narxi')
    kasbi = data.get('Kasbi')
    Murojaat_qilish_vaqti = data.get('Murojaat qilish vaqti')
    maqsad = data.get ('Maqsad') 

    
    await xabar.answer('Maqsad: \n\nMaqsadingizni qisqacha yozib bering.')

    matn = f''' Sherik kerak \n\n 🏅Sherik: {ism}, \n 📚Texnalogiya: {texnalogiya}, \n 🇺🇿Telegram: {telegram}, \n  📞Aloqa: {aloqa}, \n 🌐Hudud: {hudud}, \n 💰Narxi: {narxi}, \n 👨🏻‍💻Kasbi: {kasbi}, \n 🕰Murojaat qilish vaqti: {Murojaat_qilish_vaqti}, \n 🔎Maqsad: {maqsad} \n\n #sherik '''
    await xabar.answer(matn)
    await xabar.answer(text="Siz kiritgan ma\'lumotlaringiz to\'g\'rimi?",
                       reply_markup=inline_menu.as_markup()
                       )
    await state.set_state(Confirming.confirming)
    await state.update_data(text=matn)


@dp.callback_query(F.data == 'correct', Confirming.confirming)
async def correct_callback_query_handler(telefon: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    matn = data.get('text')


    await bot.send_message(
        chat_id=admin,
        text=matn,
        reply_markup=inline_menu.as_markup()
    )
    await telefon.answer('xabaringiz adminga yuborildi! :)')

    await telefon.message.delete()

@dp.callback_query(F.data == 'incorrect', Confirming.confirming)
async def correct_callback_query_handler(telefon: CallbackQuery, state: FSMContext):
    await telefon.answer('arizangiz bekor qilindi :(')
    await telefon.message.delete

@dp.message(F.text == 'Ish joyi kerak')
async def for_ish_joyi_kerak(xabar: Message, state: FSMContext):
    text2 = xabar.text

    print(
        text2
        )

    await state.update_data({'Xodim': text2})
    await xabar.answer('Ismingizni kiriting')
    await state.set_state(IshJoyiKerakAnketa.ism)
    

@dp.message(IshJoyiKerakAnketa.ism)
async def get_ism(xabar:Message, state: FSMContext):
    text2 = xabar.text

    print(
        text2
    )   

    await state.update_data({'Yosh': text2})
    await xabar.answer('Yosh: \n\nYoshingizni kiriting?\nMasalan, 19')
    await state.set_state(IshJoyiKerakAnketa.Texnologiya)

@dp.message(IshJoyiKerakAnketa.Texnologiya)
async def get_Texnalogiya(xabar:Message, state: FSMContext):
    text2 = xabar.text
    print(
        text2
    )
    await state.update_data({'Texnalogiya': text2})
    await xabar.answer('Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#')
    await state.set_state(IshJoyiKerakAnketa.Aloqa)


@dp.message(IshJoyiKerakAnketa.Aloqa)
async def get_Aloqa(xabar:Message, state: FSMContext):
    text2 = xabar.text
    print(
        text2
    )
    await state.update_data({'Aloqa': text2})

    await xabar.answer('Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67')
    await state.set_state(IshJoyiKerakAnketa.Hudud)

@dp.message(IshJoyiKerakAnketa.Hudud)
async def get_Hudud(xabar:Message, state: FSMContext):
    text2 = xabar.text
    print(
        text2
    )
    await state.update_data({'Hudud': text2})
    await xabar.answer('Hudud:\n\n Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.')
    await state.set_state(IshJoyiKerakAnketa.Narxi)



@dp.message(IshJoyiKerakAnketa.Narxi)
async def get_Narxi(xabar:Message, state: FSMContext):
    text2 = xabar.text
    print(
        text2
    )
    await state.update_data({'Narxi': text2})
    await xabar.answer('Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?')
    await state.set_state(IshJoyiKerakAnketa.Kasbi)

@dp.message(IshJoyiKerakAnketa.Kasbi)
async def get_Kasbi(xabar:Message, state: FSMContext):
    text2 = xabar.text
    print(
        text2
    )
    await state.update_data({'Kasbi': text2})
    await xabar.answer('Kasbi:\n\n Ishlaysizmi yoki o`qiysizmi?\nMasalan, Talaba')
    await state.set_state(IshJoyiKerakAnketa.Murojaat_qilish_vaqti)

@dp.message(IshJoyiKerakAnketa.Murojaat_qilish_vaqti)
async def get_Murojaat_qilish_vaqti(xabar:Message, state: FSMContext):
    text2 = xabar.text
    print(
        text2
    )
    await state.update_data({'Murojat qilish vaqti': text2})

    await xabar.answer('Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00')
    await state.set_state(IshJoyiKerakAnketa.Maqsad)



@dp.message(IshJoyiKerakAnketa.Maqsad)
async def get_Maqsad(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await state.update_data({'Maqsad': text})

    data = await state.get_data()

    
    ism = data.get('Xodim')
    yosh = data.get("Yosh")
    texnalogiya = data.get('Texnologiya')
    telegram = data.get('Telegram')
    aloqa = data.get('Aloqa')
    hudud = data.get('Hudud')
    narxi = data.get('Narxi')
    kasbi = data.get('Kasbi')
    Murojaat_qilish_vaqti = data.get('Murojaat qilish vaqti')
    maqsad = data.get ('Maqsad') 

    
    await xabar.answer('Maqsad: \n\nMaqsadingizni qisqacha yozib bering.')
    await state.clear()
    await state.set_state(Anketa)

    await xabar.answer(f''' Ish Joiy kerak \n\n 🏅Xodim: {ism}, \n Yosh: {yosh}, \n 📚Texnalogiya: {texnalogiya}, \n 🇺🇿Telegram: {telegram}, \n  📞Aloqa: {aloqa}, \n 🌐Hudud: {hudud}, \n 💰Narxi: {narxi}, \n 👨🏻‍💻Kasbi {kasbi}, \n 🕰Murojaat qilish vaqti {Murojaat_qilish_vaqti}, \n 🔎Maqsad {maqsad} \n\n #sherik ''')


@dp.message(F.text == 'Ustoz kerak')
async def for_ustoz_kerak(xabar: Message, state: FSMContext):
    await xabar.answer('Ismingizni kiriting')
    await state.set_state(UstozKerakAnketa.ism)


@dp.message(UstozKerakAnketa.ism)
async def get_ism(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('Yosh: \n\nYoshingizni kiriting?\nMasalan, 19')
    await state.set_state(UstozKerakAnketa.Texnologiya)

@dp.message(UstozKerakAnketa.Texnologiya)
async def get_Texnalogiya(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#')
    await state.set_state(UstozKerakAnketa.Aloqa)


@dp.message(UstozKerakAnketa.Aloqa)
async def get_Aloqa(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('📞 Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67')
    await state.set_state(UstozKerakAnketa.Hudud)

@dp.message(UstozKerakAnketa.Hudud)
async def get_Hudud(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🌐 Hudud:\n\n Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.')
    await state.set_state(UstozKerakAnketa.Narxi)



@dp.message(UstozKerakAnketa.Narxi)
async def get_Narxi(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?')
    await state.set_state(UstozKerakAnketa.Kasbi)

@dp.message(UstozKerakAnketa.Kasbi)
async def get_Kasbi(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('👨🏻‍💻 Kasbi:\n\n Ishlaysizmi yoki o`qiysizmi?\nMasalan, Talaba')
    await state.set_state(UstozKerakAnketa.Murojaat_qilish_vaqti)

@dp.message(UstozKerakAnketa.Murojaat_qilish_vaqti)
async def get_Murojaat_qilish_vaqti(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00')
    await state.set_state(UstozKerakAnketa.Maqsad)



@dp.message(UstozKerakAnketa.Maqsad)
async def get_Maqsad(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🔎 Maqsad: \n\nMaqsadingizni qisqacha yozib bering.')
    await state.set_state(UstozKerakAnketa)

@dp.message(F.text == 'Hodim kerak')
async def for_hodim_kerak(xabar: Message, state: FSMContext):
    await xabar.answer('🎓 Idora nomi?')
    await state.set_state(HodimKerakAnketa.Yosh)


@dp.message(HodimKerakAnketa.Yosh)
async def get_ism(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🕑 Yosh: \n\nYoshingizni kiriting?\nMasalan, 19')
    await state.set_state(HodimKerakAnketa.Texnologiya)

@dp.message(HodimKerakAnketa.Texnologiya)
async def get_Texnalogiya(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#')
    await state.set_state(HodimKerakAnketa.Aloqa)


@dp.message(HodimKerakAnketa.Aloqa)
async def get_Aloqa(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('📞 Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67')
    await state.set_state(HodimKerakAnketa.Hudud)

@dp.message(HodimKerakAnketa.Hudud)
async def get_Hudud(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🌐 Hudud:\n\n Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.')
    await xabar.answer('✍️Mas\'ul ism sharifi?')

    await state.set_state(HodimKerakAnketa.Murojaat_qilish_vaqti)


@dp.message(HodimKerakAnketa.Murojaat_qilish_vaqti)
async def get_Murojaat_qilish_vaqti(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00')

    await xabar.answer('🕰 Ish vaqtini kiriting?')

    await xabar.answer('💰 Maoshni kiriting?')

    await xabar.answer('‼️ Qo`shimcha ma`lumotlar?')
    await state.set_state(HodimKerakAnketa.Maqsad)



@dp.message(F.text == 'Shogird kerak')
async def for_shogird_kerak(xabar: Message, state: FSMContext):
    await xabar.answer('Ismingizni kiriting')
    await state.set_state(ShogirdKerakAnketa.Texnologiya)
   
@dp.message(ShogirdKerakAnketa.ism)
async def get_ism(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🕑 Yosh: \n\nYoshingizni kiriting?\nMasalan, 19')
    await state.set_state(ShogirdKerakAnketa.Texnologiya)

@dp.message(ShogirdKerakAnketa.Texnologiya)
async def get_Texnalogiya(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('📚 Texnologiya:\n\nTalab qilinadigan texnologiyalarni kiriting?\nTexnologiya nomlarini vergul bilan ajrating. Masalan, \n\nJava, C++, C#')
    await state.set_state(ShogirdKerakAnketa.Aloqa)


@dp.message(ShogirdKerakAnketa.Aloqa)
async def get_Aloqa(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('📞 Aloqa: \n\nBog`lanish uchun raqamingizni kiriting?\nMasalan, +998 90 123 45 67')
    await state.set_state(Anketa.Hudud)

@dp.message(ShogirdKerakAnketa.Hudud)
async def get_Hudud(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🌐 Hudud:\n\n Qaysi hududdansiz?\nViloyat nomi, Toshkent shahar yoki Respublikani kiriting.')
    await state.set_state(ShogirdKerakAnketa.Narxi)



@dp.message(ShogirdKerakAnketa.Narxi)
async def get_Narxi(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('💰 Narxi:\n\nTolov qilasizmi yoki Tekinmi?\nKerak bo`lsa, Summani kiriting?')
    await state.set_state(Anketa.Kasbi)

@dp.message(ShogirdKerakAnketa.Kasbi)
async def get_Kasbi(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('👨🏻‍💻 Kasbi:\n\n Ishlaysizmi yoki o`qiysizmi?\nMasalan, Talaba')
    await state.set_state(ShogirdKerakAnketa.Murojaat_qilish_vaqti)

@dp.message(ShogirdKerakAnketa.Murojaat_qilish_vaqti)
async def get_Murojaat_qilish_vaqti(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🕰 Murojaat qilish vaqti:\n\nQaysi vaqtda murojaat qilish mumkin?\nMasalan, 9:00 - 18:00')
    await state.set_state(ShogirdKerakAnketa.Maqsad)



@dp.message(ShogirdKerakAnketa.Maqsad)
async def get_Maqsad(xabar:Message, state: FSMContext):
    text = xabar.text
    print(
        text
    )
    await xabar.answer('🔎 Maqsad: \n\nMaqsadingizni qisqacha yozib bering.')
    await state.set_state(ShogirdKerakAnketa)




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
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

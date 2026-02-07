import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile
from aiogram.filters import Command
from config import API_KEY

async def logger(message:Message):
    print(f'[{message.chat.first_name}]: {message.text}')

bot = Bot(token = API_KEY)
dp = Dispatcher()
router = Router()

button_about = KeyboardButton(text = "Расскажи о себе")
button_posibilities = KeyboardButton(text = "Что ты умеешь?")
button_wait = KeyboardButton(text = "...")
button_start_test = KeyboardButton(text = 'Давай попробуем!')
start_reply_keyboard = ReplyKeyboardMarkup(keyboard = [[button_about],[button_posibilities]], resize_keyboard=True)
after_about_reply_keyboard = ReplyKeyboardMarkup(keyboard= [[button_posibilities]], resize_keyboard=True)
await_markup_reply_keybpard = ReplyKeyboardMarkup(keyboard=[[button_wait]],resize_keyboard=True)
start_test_reply_keyboard = ReplyKeyboardMarkup(keyboard=[[button_start_test]],resize_keyboard=True)

@router.message(Command('start'))
async def start_handler(message: Message):

    await logger(message)
    await message.answer(text = f'Привет, на связи Пандя 🐼')
    await asyncio.sleep(0.5)
    await message.answer(text = 'Я - бот Московского зоопарка.\n', reply_markup=start_reply_keyboard)


@router.message(F.text =='Расскажи о себе')
async def about_handler(message: Message):
    await logger(message)
    await message.answer(text = 'Я - житель Московского зоопарка!\nМосковский зоопарк — один из старейших зоопарков Европы.\n\nЗдесь живут самые редкие животные на нашей планете!',reply_markup=after_about_reply_keyboard)


@router.message(F.text =='Что ты умеешь?')
async def skills_handler(message: Message):
    await logger(message)
    await message.answer(text='Такс...', reply_markup=await_markup_reply_keybpard)
    await asyncio.sleep(1)
    await message.answer(text = 'Я умею спать')
    await asyncio.sleep(1)
    await message.answer(text='Кушать бамбук...')
    await asyncio.sleep(2)
    await message.answer(text='А! Я ещё гадать умею. Могу узнать твоё тотемное животное.')
    await asyncio.sleep(1)
    await message.answer(text = 'Хочешь попробовать?', reply_markup=start_test_reply_keyboard)


@router.message(F.text =='Давай попробуем!')
async def start_test(message: Message):
    photo = FSInputFile('./photo/cat-panic-help.jpg')
    await message.answer_photo(photo= photo, caption = 'Поехали')


dp.include_router(router)

async def main():
    print('bot started')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
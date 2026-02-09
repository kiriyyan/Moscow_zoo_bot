#------------------------Outer_libs-------------------------
import asyncio
from aiogram.filters import Command, callback_data
from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
#----------------------------------------------------------⯾

#------------------------Inner_libs-------------------------
from keyboards import *
#----------------------------------------------------------⯾


async def logger(message:Message):
    '''
    Logs user message history
    :param message:
    :return: None
    '''
    print(f'[{message.chat.first_name}]: {message.text}')


#------------------------States----------------------------
class bot_states(StatesGroup):
    start = State()
    quiz = State()

states = bot_states()
#----------------------------------------------------------⯾


def register_handlers(router:Router):
    router.message.register(start_handler, Command('start'))
    router.message.register(about_handler, states.start, F.text =='Расскажи о себе')
    router.message.register(skills_handler, states.start, F.text =='Что ты умеешь?')
    router.message.register(start_test, states.start, F.text =='Давай попробуем!')
    router.callback_query.register(question, states.quiz,lambda c: c.data)


#-----------------------Handlers-----------------------
async def start_handler(message: Message, state:FSMContext):
    await state.set_state(states.start)
    await logger(message)
    await message.answer(text = f'Привет, на связи Пандя 🐼')
    await asyncio.sleep(0.5)
    await message.answer(text = 'Я - бот Московского зоопарка.\n', reply_markup=start_reply_keyboard)

async def about_handler(message: Message):
    await logger(message)
    await message.answer(text = 'Я - житель Московского зоопарка!\nМосковский зоопарк — один из старейших зоопарков Европы.\n\nЗдесь живут самые редкие животные на нашей планете!',reply_markup=after_about_reply_keyboard)

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

async def start_test(message: Message, state:FSMContext):
    await state.set_state(state= states.quiz)
    # photo = FSInputFile('./photo/cat-panic-help.jpg')
    await message.answer(text = 'Поехали', reply_markup=test1_inline_keyboard)

async def question(callback: CallbackQuery, state: FSMContext):
    await callback.answer('ПОЙМАЛ КОЛБЕК')
    await state.set_data(data = {'prikol': callback.answer()})
    await callback.message.answer(f'Получил колбек {await state.get_data()}')
#----------------------------------------------------------⯾

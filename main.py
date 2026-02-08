import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command, callback_data
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup




from config import API_KEY

class bot_states(StatesGroup):
    start = State()
    quiz = State()

states = bot_states()


async def logger(message:Message):
    '''
    Logs user message history
    :param message:
    :return: None
    '''
    print(f'[{message.chat.first_name}]: {message.text}')

bot = Bot(token = API_KEY)
dp = Dispatcher()
router = Router()

#-----------------------Relpy_Buttons-----------------------
button_about = KeyboardButton(text = "Расскажи о себе")
button_posibilities = KeyboardButton(text = "Что ты умеешь?")
button_wait = KeyboardButton(text = "...")
button_start_test = KeyboardButton(text = 'Давай попробуем!')

#-----------------------Reply_Keyboards-----------------------
start_reply_keyboard = ReplyKeyboardMarkup(keyboard = [[button_about],[button_posibilities]], resize_keyboard=True)
after_about_reply_keyboard = ReplyKeyboardMarkup(keyboard= [[button_posibilities]], resize_keyboard=True)
await_markup_reply_keybpard = ReplyKeyboardMarkup(keyboard=[[button_wait]],resize_keyboard=True)
start_test_reply_keyboard = ReplyKeyboardMarkup(keyboard=[[button_start_test]],resize_keyboard=True)


#-----------------------Inline_Buttons-----------------------
button_test = InlineKeyboardButton(text = 'Вода', callback_data='#Water')

#-----------------------Inline_Keyboards-----------------------
test1_inline_keyboard = InlineKeyboardMarkup(inline_keyboard = [[button_test], [button_test]])
# test2_inline_keyboard = InlineKeyboardMarkup([[]])
# test3_inline_keyboard = InlineKeyboardMarkup([[]])
# test4_inline_keyboard = InlineKeyboardMarkup([[]])
# test5_inline_keyboard = InlineKeyboardMarkup([[]])
#-----------------------Routers-----------------------
@router.message(Command('start'))
async def start_handler(message: Message, state:FSMContext):
    await state.set_state(states.start)
    await logger(message)
    await message.answer(text = f'Привет, на связи Пандя 🐼')
    await asyncio.sleep(0.5)
    await message.answer(text = 'Я - бот Московского зоопарка.\n', reply_markup=start_reply_keyboard)


@router.message(states.start, F.text =='Расскажи о себе')
async def about_handler(message: Message):
    await logger(message)
    await message.answer(text = 'Я - житель Московского зоопарка!\nМосковский зоопарк — один из старейших зоопарков Европы.\n\nЗдесь живут самые редкие животные на нашей планете!',reply_markup=after_about_reply_keyboard)


@router.message(states.start, F.text =='Что ты умеешь?')
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


@router.message(states.start, F.text =='Давай попробуем!')
async def start_test(message: Message, state:FSMContext):
    await state.set_state(state= states.quiz)
    photo = FSInputFile('./photo/cat-panic-help.jpg')
    await message.answer_photo(photo= photo, caption = 'Поехали', reply_markup=test1_inline_keyboard)


@router.callback_query(states.quiz,lambda c: c.data)
async def question(callback: CallbackQuery, state: FSMContext):
    await callback.answer('ПОЙМАЛ КОЛБЕК')
    await state.set_data(data = {'prikol': callback.answer()})
    await bot.send_message(callback.message.chat.id, f'Получил колбек {await state.get_data()}')


dp.include_router(router)



#-----------------------Initialization-----------------------
async def main():
    print('bot started')
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
#------------------------Outer_libs-------------------------
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
#----------------------------------------------------------⯾


#-----------------------Relpy_Buttons-----------------------
button_about = KeyboardButton(text = "Расскажи о себе")
button_posibilities = KeyboardButton(text = "Что ты умеешь?")
button_wait = KeyboardButton(text = "...")
button_start_test = KeyboardButton(text = 'Давай попробуем!')
#----------------------------------------------------------⯾


#-----------------------Reply_Keyboards-----------------------
start_reply_keyboard = ReplyKeyboardMarkup(keyboard = [[button_about],[button_posibilities]], resize_keyboard=True)
after_about_reply_keyboard = ReplyKeyboardMarkup(keyboard= [[button_posibilities]], resize_keyboard=True)
await_markup_reply_keybpard = ReplyKeyboardMarkup(keyboard=[[button_wait]],resize_keyboard=True)
start_test_reply_keyboard = ReplyKeyboardMarkup(keyboard=[[button_start_test]],resize_keyboard=True)
#----------------------------------------------------------⯾


#-----------------------Inline_Buttons-----------------------
button_test = InlineKeyboardButton(text = 'Вода', callback_data='#Water')
#----------------------------------------------------------⯾


#-----------------------Inline_Keyboards-----------------------
test1_inline_keyboard = InlineKeyboardMarkup(inline_keyboard = [[button_test], [button_test]])
# test2_inline_keyboard = InlineKeyboardMarkup([[]])
# test3_inline_keyboard = InlineKeyboardMarkup([[]])
# test4_inline_keyboard = InlineKeyboardMarkup([[]])
# test5_inline_keyboard = InlineKeyboardMarkup([[]])
#----------------------------------------------------------⯾
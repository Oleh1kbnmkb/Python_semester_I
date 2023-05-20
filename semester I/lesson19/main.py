import asyncio
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor
from config import token
from poloniex import api_query

TOKEN = "6255018670:AAHDRCHL72HP0STq6oHn2WmWv6YcNtQtwoc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard_markup = keyboard()
    await message.answer('Добро пожаловать. ✌', reply_markup=keyboard_markup)

@dp.message_handler(content_types=["text"])
async def send_anytext(message: types.Message):    
    chat_id = message.chat.id
    if message.text == '📖 Баланс':
        text = '✅ Ваш баланс \n\n'
        balance = api_query('returnBalances')
        for i in balance.items():            							
            if i[1] != '0.00000000':
                print(i)
                text = text + '<b>' + i[0] + '</b>' + '\t --- \t' + i[1] + '\n'
        keyboard_markup = keyboard()
        await bot.send_message(chat_id, text, parse_mode=ParseMode.HTML, reply_markup=keyboard_markup)

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('📖 Баланс')
    markup.add(btn1)
    return markup  

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

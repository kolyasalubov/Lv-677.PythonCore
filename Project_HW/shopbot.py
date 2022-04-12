import aiohttp
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import json


bot = Bot(token='5214561248:AAHnvdHdTI7sHGhF4-sbBH9G8kc9JGqHj0U')
dp = Dispatcher(bot)

button_btc_usdt, button_eth_usdt = KeyboardButton('btc_usdt'), KeyboardButton('eth_usdt')
crypto_keyboard = ReplyKeyboardMarkup()
crypto_keyboard.add(button_btc_usdt, button_eth_usdt)


async def get_price(symbol1: str = 'BTC', symbol2: str = 'USDT'):
    url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol1}{symbol2}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()

    return json.loads(data)


def prepare_answer(data: dict):
    return '\n'.join(f'{key}: {value}' for key, value in data.items())


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hello\nWelcome to ShopBot",
                        reply_markup=crypto_keyboard)


@dp.message_handler()
async def response_message(msg: types.Message):
    currency1, currency2 = msg.text.upper().split('_')
    data = await get_price(currency1, currency2)
    await bot.send_message(msg.from_user.id, prepare_answer(data))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
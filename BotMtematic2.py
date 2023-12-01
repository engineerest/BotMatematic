import random
from aiogram.filters.command import Command
from aiogram import types, Dispatcher, Bot, Router, F
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder as IB
import asyncio
import logging
logging.basicConfig(level=logging.INFO)
router = Router()

dp = Dispatcher()
dp.include_router(router)

Token = Bot(token="&&&&&")
symbol_list = ['+', '-', '/', '*']
symbol = random.choice(symbol_list)

game = {
    "number1" : random.randint(1, 1000),
    "number2" : random.randint(1, 1000),
    "number3" : random.randint(1, 1000),
    "number4" : random.randint(1, 1000),
    "math_problem" : f"{['number1']} {symbol} {['number2']}",
    "correct_result" : 0,
    "plus_b" : 0,
    "minus_b" : 0,
    "divide_b" : 0,
    "multiply_b" : 0,
    "plus_button" : 0,
    "minus_button" : 0,
    "divide_button" : 0,
    "multiply_button" : 0
}
def refresh():
    symbol_list = ['+', '-', '/', '*']
    symbol = random.choice(symbol_list)
    game["number1"] = random.randint(1, 1000)
    game['number2'] = random.randint(1, 1000)
    game['math_problem'] = f"{game['number1' or 'number3']} {symbol} {game['number2' or 'number4']}"
    game['correct_result'] = eval(game['math_problem'])
    game['plus_b'] = f"{game['number1' or 'number3']} + {game['number2' or 'number4']}"
    game['minus_b'] = f"{game['number3']} - {game['number2']}"
    game['divide_b'] = f"{game['number1']} / {game['number4']}"
    game['multiply_b'] = f"{game['number1' or 'number3']} * {game['number2' or 'number4']}"
    game['plus_button'] = eval(game['plus_b'])
    game['minus_button'] = eval(game['minus_b'])
    game['divide_button'] = eval(game['divide_b'])
    game['multiply_button'] = eval(game['multiply_b'])
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Здравствуйте! Вы должны выбрать пример в ответ. Используйте /matematic")

async def question(message: types.Message):
    refresh()
    kb = IB()
    kb.row(
            types.InlineKeyboardButton(text=f"{game['plus_b']}", callback_data="plus"),
            types.InlineKeyboardButton(text=f"{game['minus_b']}", callback_data="minus"),
            types.InlineKeyboardButton(text=f"{game['divide_b']}", callback_data="divide"),
            types.InlineKeyboardButton(text=f"{game['multiply_b']}", callback_data="multiply"))

    await message.answer(f"{game['correct_result']}, Каков правильный пример?", reply_markup=kb.as_markup())
@dp.message(Command("matematic"))
async def matematic(message:types.Message):
    await question(message)
@router.callback_query(F.data == "plus")
async def plus(callback:types.CallbackQuery):
    if game['plus_button'] == game['correct_result']:
        await callback.message.answer(f"Верно!\n{game['correct_result']} = {game['math_problem']}")
        await callback.message.delete()
        await question(callback.message)
    else:
        await callback.message.answer(f"Неверно!\n{game['correct_result']} = {game['math_problem']}\nВаш ответ:{game['plus_b']}")
        await callback.message.delete()
        await question(callback.message)
@router.callback_query(F.data == "minus")
async def minus(callback:types.CallbackQuery):
    if game['minus_button'] == game['correct_result']:
        await callback.message.answer(f"Верно!\n{game['correct_result']} = {game['math_problem']}")
        await callback.message.delete()
        await question(callback.message)
    else:
        await callback.message.answer(f"Неверно!\n{game['correct_result']} = {game['math_problem']}")
        await callback.message.delete()
        await question(callback.message)

@router.callback_query(F.data == "divide")
async def divide(callback:types.CallbackQuery):
    if game['divide_button'] == game['correct_result']:
        await callback.message.answer(f"Верно!\n{game['correct_result']} = {game['math_problem']}")
        await callback.message.delete()
        await question(callback.message)
    else:
        await callback.message.answer(f"Неверно!\n{game['correct_result']} = {game['math_problem']}")
        await callback.message.delete()
        await question(callback.message)

@router.callback_query(F.data == "multiply")
async def multiply(callback:types.CallbackQuery):
    if game['multiply_button'] == game['correct_result']:
        await callback.message.answer(f"Верно!\n{game['correct_result']} = {game['math_problem']}")
        await callback.message.delete()
        await question(callback.message)
    else:
        await callback.message.answer(f"Неверно!\n{game['correct_result']} = {game['math_problem']}")
        await callback.message.delete()
        await question(callback.message)
@dp.message()
async def main():
    await dp.start_polling(Token)

if __name__ == "__main__":
    asyncio.run(main())

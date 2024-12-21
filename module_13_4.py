from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ''
bot = Bot(token=api)
di_p = Dispatcher(bot, storage=MemoryStorage())

@di_p.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.')

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@di_p.message_handler(text='Calories')
async def set_age(message):
    await message.answer('Введите свой возраст:')
    await UserState.age.set()

@di_p.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@di_p.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@di_p.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    male_norm = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) - 161
    female_norm = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Если Вы - мужчина, то ваша норма калорий составляет: {male_norm}.')
    await message.answer(f'Если Вы - женщина, то ваша норма калорий составляет: {female_norm}.')
    await state.finish()

@di_p.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(di_p, skip_updates=True)
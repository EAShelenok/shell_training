from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
di_p = Dispatcher(bot, storage=MemoryStorage())

key_b = ReplyKeyboardMarkup(resize_keyboard=True)
k_button_1 = KeyboardButton(text='Рассчитать')
k_button_2 = KeyboardButton(text='Информация')
key_b.add(k_button_1)
key_b.add(k_button_2)


inl_key_b = InlineKeyboardMarkup()
inl_keyb_b_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inl_keyb_b_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inl_key_b.add(inl_keyb_b_1)
inl_key_b.add(inl_keyb_b_2)

@di_p.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=inl_key_b)

@di_p.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=key_b)

@di_p.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer(f'При расчете используется формула Миффлина-Сан Жеора: \n'
                              f'1) для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5; \n'
                              f'2) для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161.')
    await call.answer()

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@di_p.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


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
    female_norm = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) - 161
    male_norm = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f'Если Вы - мужчина, то ваша норма калорий составляет: {male_norm}.')
    await message.answer(f'Если Вы - женщина, то ваша норма калорий составляет: {female_norm}.')
    await state.finish()

@di_p.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(di_p, skip_updates=True)
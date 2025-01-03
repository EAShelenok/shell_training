from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

initiate_db()

api = ''
bot = Bot(token=api)
di_p = Dispatcher(bot, storage=MemoryStorage())

key_b = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')],
        [KeyboardButton(text='Регистрация')]
    ],
    resize_keyboard=True
)

inl_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 3',callback_data='product_buying'),
         InlineKeyboardButton(text='Продукт 4',callback_data='product_buying'),
        ]
    ]
)

inl_key_b = InlineKeyboardMarkup()
inl_keyb_b_1 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
inl_keyb_b_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inl_key_b.add(inl_keyb_b_1)
inl_key_b.add(inl_keyb_b_2)

@di_p.message_handler(text='Купить')
async def get_buying_list(message):
    #for i in range(4):
    #    await message.answer(f'Название: Продукт {i + 1} | Описание: {i + 1} | Цена: {(i + 1) * 100}')
    for item in get_all_products():
        await message.answer(f'Название: {item[1]} | Описание: {item[2]} | Цена: {item[3]}')
        with open(f'pic/{item[0]}.png', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки:', reply_markup=inl_menu)

@di_p.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

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

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = State()

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

@di_p.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@di_p.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_uncluded(message.text):
        await message.answer('Пользователь существует, введите другое имя:')
        await RegistrationState.username.set()
    else:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()

@di_p.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@di_p.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    u_data = await state.get_data()
    add_user(u_data['username'], u_data['email'], u_data['age'])
    await message.answer('Пользователь успешно зарегистрирован!', reply_markup=key_b)
    await state.finish()

@di_p.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(di_p, skip_updates=True)
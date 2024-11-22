from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = "Свой токен"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

# Класс для состояний пользователя
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Создание клавиатуры
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    types.KeyboardButton("Рассчитать"),
    types.KeyboardButton("Информация")
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот, помогающий рассчитать норму калорий. Выберите действие:",
        reply_markup=keyboard  # Отправляем клавиатуру
    )

@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def set_age(message: types.Message):
    await UserState.age.set()
    await message.answer("Введите свой возраст:")

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите число.")
        return
    await state.update_data(age=int(message.text))
    await UserState.growth.set()
    await message.answer("Введите свой рост (в сантиметрах):")

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите число.")
        return
    await state.update_data(growth=int(message.text))
    await UserState.weight.set()
    await message.answer("Введите свой вес (в килограммах):")

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите число.")
        return
    await state.update_data(weight=int(message.text))

    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    calories = 88.36 + (13.4 * weight) + (4.8 * growth) - (5.7 * age)

    await message.answer(f"Ваша норма калорий: {int(calories)} ккал.")

    await state.finish()

@dp.message_handler(lambda message: message.text.lower() == 'информация')
async def send_info(message: types.Message):
    await message.answer("Я помогаю рассчитать норму калорий. Нажмите 'Рассчитать', чтобы начать.")

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Пожалуйста, выберите действие с помощью кнопок на клавиатуре. Для взаимодействия введите /start")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

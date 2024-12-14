from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = "Свой токен"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    types.KeyboardButton("Рассчитать"),
    types.KeyboardButton("Информация")
)

inline_keyboard = types.InlineKeyboardMarkup()
inline_keyboard.add(
    types.InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories'),
    types.InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот, помогающий твоему здоровью.",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    await message.answer(
        "Выберите опцию:",
        reply_markup=inline_keyboard
    )

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = (
        "10×вес(кг) + 6.25×рост(см) - 5×возраст(г) - 161\n"
    )
    await call.message.answer(formula)

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")

@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=int(message.text))
    await UserState.growth.set()
    await message.answer("Введите свой рост (в сантиметрах):")

@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=int(message.text))
    await UserState.weight.set()
    await message.answer("Введите свой вес (в килограммах):")

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']

    calories = 10 * weight + 6.25 * growth - 5 * age- 161
    await message.answer(f"Ваша норма калорий: {calories:.1f} ккал.")

    await state.finish()

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите 'Рассчитать' для подсчёта нормы калорий или выберите 'Информация'.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
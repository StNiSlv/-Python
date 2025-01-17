from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

api = "свой токен"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

# Главное меню
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(
    types.KeyboardButton("Рассчитать"),
    types.KeyboardButton("Информация"),
    types.KeyboardButton("Купить")
)
product_names = ['Кормилица', 'Deko', 'Global Village', 'Bonduelle']
product_descriptions = ['Топ за свои деньги', 'Средне', 'Вкусно', 'Дорого']
product_prices = [100, 200, 300, 400]
product_images = [
        "https://avatars.mds.yandex.net/i?id=2303f16391ebb7ffb1d9f4f0def6b560_l-5220445-images-thumbs&n=13",
        "https://detivmagazine.ru/wp-content/uploads/7/a/b/7ab69fa5711d6b633de4ff70d9cfbb81.jpeg",
        "https://otzivi-tut.ru/upload/iblock/643/643db00ac70de60691c45445e5472002.jpeg",
        "https://sirvmasle.ru/upload/iblock/ad8/pf1ladbig3qqqjw6cls3qezel05fl4yv.jpg",
]

inline_buy_keyboard = types.InlineKeyboardMarkup()
for i in range(1, 5):
    inline_buy_keyboard.add(
        types.InlineKeyboardButton(f"{product_names[i-1]}", callback_data="product_buying")
    )

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот, помогающий твоему здоровью.",
        reply_markup=keyboard
    )

@dp.message_handler(lambda message: message.text.lower() == 'рассчитать')
async def main_menu(message: types.Message):
    inline_keyboard = types.InlineKeyboardMarkup()
    inline_keyboard.add(
        types.InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories'),
        types.InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
    )
    await message.answer(
        "Выберите опцию:",
        reply_markup=inline_keyboard
    )

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    formula = "10×вес(кг) + 6.25×рост(см) - 5×возраст(г) - 161\n"
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

    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f"Ваша норма калорий: {calories:.1f} ккал.")
    await state.finish()

@dp.message_handler(lambda message: message.text.lower() == 'купить')
async def get_buying_list(message: types.Message):
    product_names = ['Кормилица', 'Deko', 'Global Village', 'Bonduelle']
    product_descriptions = ['Топ за свои деньги', 'Средне', 'Вкусно', 'Дорого']
    product_prices = [100, 200, 300, 400]
    product_images = [
        "https://avatars.mds.yandex.net/i?id=2303f16391ebb7ffb1d9f4f0def6b560_l-5220445-images-thumbs&n=13",
        "https://detivmagazine.ru/wp-content/uploads/7/a/b/7ab69fa5711d6b633de4ff70d9cfbb81.jpeg",
        "https://otzivi-tut.ru/upload/iblock/643/643db00ac70de60691c45445e5472002.jpeg",
        "https://sirvmasle.ru/upload/iblock/ad8/pf1ladbig3qqqjw6cls3qezel05fl4yv.jpg",
    ]

    for i in range(4):
        await message.answer_photo(
            photo=product_images[i],
            caption=f"Название: {product_names[i]} | Описание: {product_descriptions[i]} | Цена: {product_prices[i]} ₽"
        )
    await message.answer("Выберите продукт для покупки:", reply_markup=inline_buy_keyboard)

@dp.callback_query_handler(lambda call: call.data == "product_buying")
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите 'Рассчитать' для подсчёта нормы калорий или выберите 'Информация'.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
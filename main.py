import sqlite3
import aiogram


from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.filters import Text


from kb import *

bot = Bot("5802680214:AAEJqkpuS3k8cHYdQg9trqERtlCm8a2pLDk")
dp = Dispatcher(bot)

conn = sqlite3.connect('engEz.db')
c = conn.cursor()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await message.answer(text="Привет!\nЯ буду твоим учителем английского языка в Telegram\nМы будем общаться с помощью кнопок. Нажимай.", reply_markup=kb)
	await message.delete()

@dp.message_handler(Text(equals="Погнали!"))
async def second_start(message: types.Message):
	await message.answer(text="Рады тебя видеть!\nНам нужно немного информации перед началом\n Для начала выбери категорию, для чего тебе нужен английский в данный момент", reply_markup=kb2)

@dp.message_handler(Text(equals="Для себя"))
async def catrgories(message: types.Message):
	await message.answer(text='Отлично! Теперь для изучения категории "Для себя" требуется указать как ты оцениваешь свой уровень английского', reply_markup=kb3)

# Добавим список для хранения идентификаторов сообщений бота
bot_messages = []

@dp.message_handler(Text(equals="Базовый"))
async def handle_basic_level(message: types.Message):
	await message.answer(text='Отлично! Теперь для изучения Базового уровня выбери категорию английских слов!', reply_markup=kb10)

@dp.message_handler(Text(equals="Средний"))
async def handle_basic_level(message: types.Message):
	await message.answer(text='Отлично! Теперь для изучения Среднего уровня выбери категорию английских слов!', reply_markup=kb11)

@dp.message_handler(Text(equals="Профессиональный"))
async def handle_basic_level(message: types.Message):
	await message.answer(text='Отлично! Теперь для изучения Среднего уровня выбери категорию английских слов!', reply_markup=kb12)

@dp.message_handler(Text(equals="Эмоции"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_hard_emotions_feelings')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Природа"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_hard_nature')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Тело"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_hard_body')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)


@dp.message_handler(Text(equals="Одежда"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_medium_clothes')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Семья"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_medium_family')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Хобби"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_medium_hobbies')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Транспорт"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_medium_transport')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Общение"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_basic_communication')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Животные"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_basic_animal')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Еда"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_basic_eat')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Цвета"))
async def handle_basic_level(message: types.Message):
		c.execute('SELECT * FROM myself_basic_colorandnumer')
		rows = c.fetchall()
		for row in rows:
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(row, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Я запомнил. Дальше!"))
async def delete_bot_messages(message: types.Message):
	# Удалим все сообщения бота из списка по одному

	# Очистим список
	bot_messages.clear()

	await message.answer(text="Начинаем тест!")
	await message.answer(text="Как на русском будет 'House' ", reply_markup=kb7)

@dp.message_handler(Text(equals="Дома"))
async def delete_bot_messages(message: types.Message):
	await message.answer(text="Гений все верно")
	await message.answer(text="Как на русском будет 'Dog' ", reply_markup=kb8)
@dp.message_handler(Text(equals="Особняки"))
async def delete_bot_messages(message: types.Message):
	await message.answer(text="Не правильно")

@dp.message_handler(Text(equals="Квартиры"))
async def delete_bot_messages(message: types.Message):
	await message.answer(text="Не правильно")

@dp.message_handler(Text(equals="Унитаз"))
async def delete_bot_messages(message: types.Message):
	await message.answer(text="Не правильно")

@dp.message_handler(Text(equals="Собака"))
async def delete_bot_messages(message: types.Message):
	await message.answer(text="Гений все верно")
	await message.answer(text="Как на русском будет 'Cat' ", reply_markup=kb9)

@dp.message_handler(Text(equals="Мама Андрея"))
async def delete_bot_messages(message: types.Message):
	await message.answer(text="Не совсем так, но мне нравится твой настрой <3 ")

@dp.message_handler(Text(equals="Кошка"))
async def delete_bot_messages(message: types.Message):
	await message.answer(text="Гений все верно")
	await message.answer(text="Бро, ты прошел весь тест, пора расти...",reply_markup=kb3)

@dp.message_handler(Text(equals="СКатЕртЬ"))
async def delete_bot_messages(message: types.Message):
	await message.answer(text="Не правильно")

@dp.message_handler(Text(equals="Папа андрея!?"))
async def delete_bot_messages(message: types.Message):
	await message.answer(text="Неее, брат, Это перебор уже... Фу..")

current_word_index = 0
words = []

@dp.message_handler(Text(equals="В главное меню"))
async def return_to_main_menu(message: types.Message):
	await message.answer(text='Вы в главном меню', reply_markup=kb2)

if __name__ == "__main__":
	executor.start_polling(dp)
import sqlite3
import aiogram
import logic

from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.filters import Text


from kb import *

bot = Bot("5802680214:AAEJqkpuS3k8cHYdQg9trqERtlCm8a2pLDk")
dp = Dispatcher(bot)

conn = sqlite3.connect('engEz.db')
c = conn.cursor()

class User():
	def __init__(self,id,communication_score,dialog_score,help_score,eat_score,place_score,sport_score,prog_score,
				 enginere_score,guide_score,economy_score,stuart_score,emodji_score,nature_score,body_score,clothes_score,
				 famaly_score,hobby_score,transport_score,animal_score,colors_score,mode):
		self.id = id
		self.communication_score = communication_score
		self.dialog_score = dialog_score
		self.help_score = help_score
		self.eat_score = eat_score
		self.place_score = place_score
		self.sport_score = sport_score
		self.prog_score = prog_score
		self.enginere_score = enginere_score
		self.guide_score = guide_score
		self.economy_score = economy_score
		self.stuart_score = stuart_score
		self.emodji_score =emodji_score
		self.nature_score = nature_score
		self.body_score = body_score
		self.clothes_score = clothes_score
		self.famaly_score = famaly_score
		self.hobby_score = hobby_score
		self.transport_score = transport_score
		self.animal_score = animal_score
		self.colors_score = colors_score
		self.mode = mode

users = []

# communication_score = 1
# dilog_score = 1
# help_score = 1
# eat_score = 1
# place_score = 1
# sport_score = 1
# prog_score = 1
# guide_score =1
# enginere_score = 1
# economy_score = 1
# stuart_score = 1
# emodji_score = 1
# nature_score = 1
# body_score = 1
# clothes_score = 1
# famaly_score = 1
# hobby_score = 1
# transport_score = 1
# animal_score = 1
# colors_score = 1


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	await message.answer(text="Привет!\nЯ буду твоим учителем английского языка в Telegram\nМы будем общаться с помощью кнопок. Нажимай.", reply_markup=kb)
	await message.delete()
	flag = 0
	for user in users:
		if user.id == message.from_user.id:
			flag = 1
			break
	if flag == 0:
		users.append(User(id=message.from_user.id, communication_score = 1, dialog_score = 1, help_score = 1, eat_score = 1,
						   place_score = 1, sport_score = 1, prog_score = 1, guide_score = 1, enginere_score = 1, economy_score = 1,
						   stuart_score = 1, emodji_score =1 ,nature_score=1,body_score = 1, clothes_score=1, famaly_score=1, hobby_score=1,
						   transport_score =1, animal_score=1, colors_score=1, mode = None))

@dp.message_handler(Text(equals="Погнали!"))
async def second_start(message: types.Message):
	await message.answer(text="Рады тебя видеть!\nНам нужно немного информации перед началом\n Для начала выбери категорию, для чего тебе нужен английский в данный момент", reply_markup=kb2)

@dp.message_handler(Text(equals="Для себя"))
async def catrgories(message: types.Message):
	await message.answer(text='Отлично! Теперь для изучения категории "Для себя" требуется указать как ты оцениваешь свой уровень английского', reply_markup=kb3)

@dp.message_handler(Text(equals="Для путешествия"))
async def catrgories(message: types.Message):
	await message.answer(text='Отлично! Теперь для изучения категории "Для путешествия" требуется указать что именно в путешествии ты хочешь узнать', reply_markup=kb13)

@dp.message_handler(Text(equals="Для профессии"))
async def catrgories(message: types.Message):
	await message.answer(text='Отлично! Теперь для изучения категории "Для профессии" требуется указать какую сферу ты хочешь изучить', reply_markup=kb14)


# Добавим список для хранения идентификаторов сообщений бота
bot_messages = []

####################################################################################
@dp.message_handler(Text(equals="Диалог"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM travel_about_myself where id ="{user.dialog_score}"')
			rows = c.fetchone()
			user.mode = 'dialog'
			user.dialog_score += 1
			massage = logic.request_in_massage(rows)
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Вопросы для помощи"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM travel_answer_for_help where id ="{user.help_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
				# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)
			user.help_score += 1
			user.mode = 'help'


@dp.message_handler(Text(equals="Места"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM travel_local where id ="{user.place_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.place_score += 1
				# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)
			user.mode = 'place'



@dp.message_handler(Text(equals="Спорт"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM prof_sport where id ="{user.sport_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.sport_score += 1

			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)
			user.mode = 'sport'

@dp.message_handler(Text(equals="Программирование"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM prof_programmer where id = "{user.prog_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.prog_score += 1
			user.mode = 'prog'

			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Гид"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM prof_gids where id = "{user.guide_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.guide_score += 1
			user.mode = 'guide'
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Инженер"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM prof_engineer where id = "{user.enginere_score}"')

			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.enginere_score += 1
			user.mode = 'enginere'
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Экономист"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM prof_economy where id = "{user.economy_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.economy_score +=1
			user.mode ='economy'
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Стюарт"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM prof_avia where id = "{user.stuart_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.stuart_score+=1
			user.mode = 'stuart'
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

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
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_hard_emotions_feelings where id = "{user.emodji_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.emodji_score += 1
			user.mode = 'emodji'
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Природа"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_hard_nature where id = "{user.nature_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.nature_score += 1
			user.mode = 'nature'
				# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Тело"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_hard_body where id = "{user.body_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.body_score += 1
			user.mode = 'body'
				# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)


@dp.message_handler(Text(equals="Одежда"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_medium_clothes where id = "{user.clothes_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.clothes_score += 1
			user.mode = 'clothes'

			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Семья"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_medium_family where id = "{user.famaly_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.famaly_score += 1
			user.mode = 'famaly'

			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Хобби"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_medium_hobbies where id = "{user.hobby_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.hobby_score += 1
			user.mode = 'hobby'
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Транспорт"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_medium_transport where id = "{user.transport_score}"')
			rows = c.fetchone()
			massage = logic.request_in_massage(rows)
			user.transport_score += 1
			user.mode = 'transport'
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Общение"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_basic_communication where id ="{user.communication_score}"')
			rows = c.fetchone()
			user.communication_score+=1
			user.mode = 'communication'
			massage = logic.request_in_massage(rows)
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

			# Сохраним идентификатор каждого сообщения бота в список

@dp.message_handler(Text(equals="Животные"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_basic_animal where id = "{user.animal_score}"')
			rows = c.fetchone()
			user.animal_score += 1
			user.mode = 'animal'
			massage = logic.request_in_massage(rows)
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Еда"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_basic_eat where id = "{user.eat_score}"')
			rows = c.fetchone()
			user.eat_score += 1
			user.mode = 'eat'
			massage = logic.request_in_massage(rows)
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Цвета"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			c.execute(f'SELECT * FROM myself_basic_colorandnumer where id = "{user.colors_score}"')
			rows = c.fetchone()
			user.colors_score += 1
			user.mode = 'colors'
			massage = logic.request_in_massage(rows)
			# Сохраним идентификатор каждого сообщения бота в список
			bot_message = await message.answer(massage, reply_markup=kb5)
			bot_messages.append(bot_message.message_id)

@dp.message_handler(Text(equals="Я запомнил. Дальше!"))
async def delete_bot_messages(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'communication':
				c.execute(f'SELECT * FROM myself_basic_communication where id ="{user.communication_score}"')
				rows = c.fetchone()
				user.communication_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'colors':
				c.execute(f'SELECT * FROM myself_basic_colorandnumer where id ="{user.colors_score}"')
				rows = c.fetchone()
				user.colors_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'eat':
				c.execute(f'SELECT * FROM myself_basic_eat where id ="{user.eat_score}"')
				rows = c.fetchone()
				user.eat_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'animal':
				c.execute(f'SELECT * FROM myself_basic_animal where id ="{user.animal_score}"')
				rows = c.fetchone()
				user.animal_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'transport':
				c.execute(f'SELECT * FROM myself_medium_transport where id ="{user.transport_score}"')
				rows = c.fetchone()
				user.transport_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'hobby':
				c.execute(f'SELECT * FROM myself_medium_hobbies where id ="{user.hobby_score}"')
				rows = c.fetchone()
				user.hobby_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'famaly':
				c.execute(f'SELECT * FROM myself_medium_family where id ="{user.famaly_score}"')
				rows = c.fetchone()
				user.famaly_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")


			if user.mode == 'clothes':
				c.execute(f'SELECT * FROM myself_medium_clothes where id ="{user.clothes_score}"')
				rows = c.fetchone()
				user.clothes_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'body':
				c.execute(f'SELECT * FROM myself_hard_body where id ="{user.body_score}"')
				rows = c.fetchone()
				user.body += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'nature':
				c.execute(f'SELECT * FROM myself_hard_nature  where id ="{user.nature_score}"')
				rows = c.fetchone()
				user.nature_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'emodji':
				c.execute(f'SELECT * FROM myself_hard_emotions_feelings where id ="{user.emodji_score}"')
				rows = c.fetchone()
				user.emodji_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'stuart':
				c.execute(f'SELECT * FROM prof_avia where id ="{user.stuart_score}"')
				rows = c.fetchone()
				user.stuart_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'economy':
				c.execute(f'SELECT * FROM prof_economy where id ="{user.economy_score}"')
				rows = c.fetchone()
				user.economy_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'enginere':
				c.execute(f'SELECT * FROM prof_engineer where id ="{user.enginere_score}"')
				rows = c.fetchone()
				user.enginere_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'guide':
				c.execute(f'SELECT * FROM prof_gids where id ="{user.guide_score}"')
				rows = c.fetchone()
				user.guide_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'prog':
				c.execute(f'SELECT * FROM prof_programmer where id ="{user.prog_score}"')
				rows = c.fetchone()
				user.prog_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'sport':
				c.execute(f'SELECT * FROM prof_sport where id ="{user.sport_score}"')
				rows = c.fetchone()
				user.sport_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'place':
				c.execute(f'SELECT * FROM travel_local where id ="{user.place_score}"')
				rows = c.fetchone()
				user.place_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'dialog':
				c.execute(f'SELECT * FROM travel_about_myself where id ="{user.dialog_score}"')
				rows = c.fetchone()
				user.dialog_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")

			if user.mode == 'help':
				c.execute(f'SELECT * FROM travel_answer_for_help where id ="{user.help_score}"')
				rows = c.fetchone()
				user.help_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					print(massage)
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")


current_word_index = 0
words = []

@dp.message_handler(Text(equals="В главное меню"))
async def return_to_main_menu(message: types.Message):
	await message.answer(text='Вы в главном меню', reply_markup=kb2)

if __name__ == "__main__":
	executor.start_polling(dp)
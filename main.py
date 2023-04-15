import sqlite3
import aiogram
import logic

from aiogram import Bot, executor, Dispatcher, types
from aiogram.dispatcher.filters import Text

import random

from kb import *

bot = Bot("5802680214:AAEJqkpuS3k8cHYdQg9trqERtlCm8a2pLDk")
dp = Dispatcher(bot)

conn = sqlite3.connect('engEz.db')
c = conn.cursor()

class User():
	def __init__(self,id,communication_score,dialog_score,help_score,eat_score,place_score,sport_score,prog_score,
				 enginere_score,guide_score,economy_score,stuart_score,emodji_score,nature_score,body_score,clothes_score,
				 famaly_score,hobby_score,transport_score,animal_score,colors_score,mode,l,i):
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
		self.l = l
		self.i = i

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
						   transport_score =1, animal_score=1, colors_score=1, mode = None,l = None,i=0))

@dp.message_handler(Text(equals="Погнали!"))
async def second_start(message: types.Message):
	await message.answer(text="Рады тебя видеть!\nНам нужно немного информации перед началом\n Для начала выбери категорию, для чего тебе нужен английский в данный момент", reply_markup=kb2)
	flag = 0
	for user in users:
		if user.id == message.from_user.id:
			flag = 1
			break
	if flag == 0:
		users.append(User(id=message.from_user.id, communication_score=1, dialog_score=1, help_score=1, eat_score=1,
						  place_score=1, sport_score=1, prog_score=1, guide_score=1, enginere_score=1, economy_score=1,
						  stuart_score=1, emodji_score=1, nature_score=1, body_score=1, clothes_score=1, famaly_score=1,
						  hobby_score=1,
						  transport_score=1, animal_score=1, colors_score=1, mode=None, l=None, i=0))
@dp.message_handler(Text(equals="Для себя"))
async def catrgories(message: types.Message):
	await message.answer(text='Отлично! Теперь для изучения категории "Для себя" требуется указать как ты оцениваешь свой уровень английского', reply_markup=kb15)
	flag = 0
	for user in users:
		if user.id == message.from_user.id:
			flag = 1
			user.mode = 'myself'
			break
	if flag == 0:
		users.append(User(id=message.from_user.id, communication_score=1, dialog_score=1, help_score=1, eat_score=1,
						  place_score=1, sport_score=1, prog_score=1, guide_score=1, enginere_score=1, economy_score=1,
						  stuart_score=1, emodji_score=1, nature_score=1, body_score=1, clothes_score=1, famaly_score=1,
						  hobby_score=1,
						  transport_score=1, animal_score=1, colors_score=1, mode='myself', l=None, i=0))
@dp.message_handler(Text(equals="Для путешествия"))
async def catrgories(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			await message.answer(text='Отлично! Теперь для изучения категории "Для путешествия" требуется указать что именно в путешествии ты хочешь узнать', reply_markup=kb15)
			user.mode = 'travel'

@dp.message_handler(Text(equals="Для профессии"))
async def catrgories(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			await message.answer(text='Отлично! Теперь для изучения категории "Для профессии" требуется указать какую сферу ты хочешь изучить', reply_markup=kb15)
			user.mode = 'prof'

# Добавим список для хранения идентификаторов сообщений бота
bot_messages = []

####################################################################################
@dp.message_handler(Text(equals="Диалог"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM travel_about_myself where id ="{user.dialog_score}"')
				rows = c.fetchone()
				user.mode = 'dialog'
				user.dialog_score += 1
				massage = logic.request_in_massage(rows)
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM travel_about_myself").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_dialog_1'


			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_travel_about_myself').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_travel_about_myself where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_dialog'

@dp.message_handler(Text(equals="Вопросы для помощи"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM travel_answer_for_help where id ="{user.help_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
					# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)
				user.help_score += 1
				user.mode = 'help'

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM travel_answer_for_help").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_help_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_travel_answer_for_help').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_travel_answer_for_help where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_help'

@dp.message_handler(Text(equals="Места"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM travel_local where id ="{user.place_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.place_score += 1
					# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)
				user.mode = 'place'

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM travel_local").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_place_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_travel_local').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_travel_local where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_place'

@dp.message_handler(Text(equals="Спорт"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM prof_sport where id ="{user.sport_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.sport_score += 1

				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)
				user.mode = 'sport'

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM prof_sport").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_sport_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_prof_sport').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_prof_sport where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_sport'

@dp.message_handler(Text(equals="Программирование"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM prof_programmer where id = "{user.prog_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.prog_score += 1
				user.mode = 'prog'

				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)


			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM prof_programmer").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_prog_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_prof_programmer').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_prof_programmer where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_prog'

@dp.message_handler(Text(equals="Гид"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM prof_gids where id = "{user.guide_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.guide_score += 1
				user.mode = 'guide'
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM prof_gids").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_guide_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_prof_gids').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_prof_gids where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_guide'

@dp.message_handler(Text(equals="Инженер"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM prof_engineer where id = "{user.enginere_score}"')

				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.enginere_score += 1
				user.mode = 'enginere'
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM prof_engineer").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_enginere_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_prof_engineer').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_prof_engineer where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_enginere'

@dp.message_handler(Text(equals="Экономист"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM prof_economy where id = "{user.economy_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.economy_score +=1
				user.mode ='economy'
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM prof_economy").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_economy_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_prof_economy').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_prof_economy where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_economy'

@dp.message_handler(Text(equals="Стюарт"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM prof_avia where id = "{user.stuart_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.stuart_score+=1
				user.mode = 'stuart'
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM prof_avia").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_stuart_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_prof_avia').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_prof_avia where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_stuart'

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
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM myself_hard_emotions_feelings where id = "{user.emodji_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.emodji_score += 1
				user.mode = 'emodji'
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM myself_hard_emotions_feelings").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_emodji_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_hard_emotions_feelings').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_hard_emotions_feelings where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_emodji'

@dp.message_handler(Text(equals="Природа"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM myself_hard_nature where id = "{user.nature_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.nature_score += 1
				user.mode = 'nature'
					# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM myself_hard_nature").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_nature_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_hard_nature').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_hard_nature where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_nature'

@dp.message_handler(Text(equals="Тело"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode =='modul1':
				c.execute(f'SELECT * FROM myself_hard_body where id = "{user.body_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.body_score += 1
				user.mode = 'body'
					# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':

				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(text=f'Набирите слово {c.execute("SELECT * FROM myself_hard_body").fetchall()[0][2]} на английском', reply_markup=kb)

				user.mode = 'test_body_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_hard_body').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_hard_body where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_body'

@dp.message_handler(Text(equals="Одежда"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode =='modul1':
				c.execute(f'SELECT * FROM myself_medium_clothes where id = "{user.clothes_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.clothes_score += 1
				user.mode = 'clothes'

				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(
					text=f'Набирите слово {c.execute("SELECT * FROM myself_medium_clothes").fetchall()[0][2]} на английском',
					reply_markup=kb)

				user.mode = 'test_clothes_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_medium_clothes').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_medium_clothes where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_clothes'

@dp.message_handler(Text(equals="Семья"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM myself_medium_family where id = "{user.famaly_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.famaly_score += 1
				user.mode = 'famaly'

				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)


			if user.mode == 'modul2':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(
					text=f'Набирите слово {c.execute("SELECT * FROM myself_medium_family").fetchall()[0][2]} на английском',
					reply_markup=kb)

				user.mode = 'test_family_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_medium_family').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_medium_family where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_family'

@dp.message_handler(Text(equals="Хобби"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM myself_medium_hobbies where id = "{user.hobby_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.hobby_score += 1
				user.mode = 'hobby'
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(
					text=f'Набирите слово {c.execute("SELECT * FROM myself_medium_hobbies").fetchall()[0][2]} на английском',
					reply_markup=kb)

				user.mode = 'test_hobbies_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_medium_hobbies').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_medium_hobbies where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_hobbies'

@dp.message_handler(Text(equals="Транспорт"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode =='modul1':
				c.execute(f'SELECT * FROM myself_medium_transport where id = "{user.transport_score}"')
				rows = c.fetchone()
				massage = logic.request_in_massage(rows)
				user.transport_score += 1
				user.mode = 'transport'
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(
					text=f'Набирите слово {c.execute("SELECT * FROM myself_medium_transport").fetchall()[0][2]} на английском',
					reply_markup=kb)

				user.mode = 'test_transport_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_medium_transport').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_medium_transport where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_transport'

@dp.message_handler(Text(equals="Общение"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			print(user.mode)
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM myself_basic_communication where id ="{user.communication_score}"')
				rows = c.fetchone()
				user.communication_score+=1
				user.mode = 'communication'
				massage = logic.request_in_massage(rows)
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)
			if user.mode == 'modul2':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(
					text=f'Набирите слово {c.execute("SELECT * FROM myself_basic_communication").fetchall()[0][2]} на английском',
					reply_markup=kb)

				user.mode = 'test_communication_1'
			if user.mode =='modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_basic_communication').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_basic_communication where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))
				print(list(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text='В главное меню')
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_communication'

			# Сохраним идентификатор каждого сообщения бота в список

@dp.message_handler(Text(equals="Животные"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode=='modul1':
				c.execute(f'SELECT * FROM myself_basic_animal where id = "{user.animal_score}"')
				rows = c.fetchone()
				user.animal_score += 1
				user.mode = 'animal'
				massage = logic.request_in_massage(rows)
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(
					text=f'Набирите слово {c.execute("SELECT * FROM myself_basic_animal").fetchall()[0][2]} на английском',
					reply_markup=kb)

				user.mode = 'test_animal_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_basic_animals').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_basic_animals where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_animal'

@dp.message_handler(Text(equals="Еда"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode == 'modul1':
				c.execute(f'SELECT * FROM myself_basic_eat where id = "{user.eat_score}"')
				rows = c.fetchone()
				user.eat_score += 1
				user.mode = 'eat'
				massage = logic.request_in_massage(rows)
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)


			if user.mode == 'modul2':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(
					text=f'Набирите слово {c.execute("SELECT * FROM myself_basic_eat").fetchall()[0][2]} на английском',
					reply_markup=kb)

				user.mode = 'test_eat_1'

			if user.mode =='modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_travel_about_myself').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_basic_eat where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_eat'

@dp.message_handler(Text(equals="Цвета"))
async def handle_basic_level(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:
			if user.mode =='modul1':
				c.execute(f'SELECT * FROM myself_basic_colorandnumer where id = "{user.colors_score}"')
				rows = c.fetchone()
				user.colors_score += 1
				user.mode = 'colors'
				massage = logic.request_in_massage(rows)
				# Сохраним идентификатор каждого сообщения бота в список
				bot_message = await message.answer(massage, reply_markup=kb5)
				bot_messages.append(bot_message.message_id)

			if user.mode == 'modul2':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)

				await message.answer(
					text=f'Набирите слово {c.execute("SELECT * FROM myself_basic_colorandnumer").fetchall()[0][2]} на английском',
					reply_markup=kb)

				user.mode = 'test_colorandnumer_1'

			if user.mode == 'modul3':
				user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_travel_about_myself').fetchall()) - 1))

				c.execute(f'SELECT * FROM test_myself_basic_colorandnumer where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				rows2 = random.sample(rows, len(rows))

				k = ReplyKeyboardMarkup(resize_keyboard=True)
				b1 = KeyboardButton(text=rows2[1])
				b2 = KeyboardButton(text=rows2[2])
				b3 = KeyboardButton(text=rows2[3])
				b4 = KeyboardButton(text=rows2[4])
				b5 = KeyboardButton(text=rows2[0])
				k.add(b1, b2, b3, b4, b5)

				await message.answer(text="Составьте верное предложение из данных слов", reply_markup=k)

				user.mode = 'test_colorandnumer'

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
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:
					# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (len(c.execute(f'SELECT * FROM test_myself_basic_communication_0').fetchall()) -1 ))

					c.execute(f'SELECT * FROM test_myself_basic_communication_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text = 'В главное меню')
					k.add(b1, b2, b3, b4,b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_communication'

			if user.mode == 'colors':
				c.execute(f'SELECT * FROM myself_basic_colorandnumer where id ="{user.colors_score}"')
				rows = c.fetchone()
				user.colors_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:# Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
								len(c.execute(f'SELECT * FROM test_myself_basic_colorandnumer_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_basic_colorandnumer_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_colorandnumer'
			if user.mode == 'eat':
				c.execute(f'SELECT * FROM myself_basic_eat where id ="{user.eat_score}"')
				rows = c.fetchone()
				user.eat_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_myself_basic_eat_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_basic_eat_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_eat'


			if user.mode == 'animal':
				c.execute(f'SELECT * FROM myself_basic_animal where id ="{user.animal_score}"')
				rows = c.fetchone()
				user.animal_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_myself_basic_animals_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_basic_animals_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_animal'

			if user.mode == 'transport':
				c.execute(f'SELECT * FROM myself_medium_transport where id ="{user.transport_score}"')
				rows = c.fetchone()
				user.transport_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_myself_medium_transport_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_medium_transport_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_transport'

			if user.mode == 'hobby':
				c.execute(f'SELECT * FROM myself_medium_hobbies where id ="{user.hobby_score}"')
				rows = c.fetchone()
				user.hobby_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_myself_medium_hobbies_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_medium_hobbies_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)
					user.mode = '0_test_hobbies'

			if user.mode == 'famaly':
				c.execute(f'SELECT * FROM myself_medium_family where id ="{user.famaly_score}"')
				rows = c.fetchone()
				user.famaly_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_myself_medium_family_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_medium_family_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_family'

			if user.mode == 'clothes':
				c.execute(f'SELECT * FROM myself_medium_clothes where id ="{user.clothes_score}"')
				rows = c.fetchone()
				user.clothes_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_myself_medium_clothes_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_medium_clothes_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_clothes'

			if user.mode == 'body':
				c.execute(f'SELECT * FROM myself_hard_body where id ="{user.body_score}"')
				rows = c.fetchone()
				user.body_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_myself_hard_body_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_hard_body_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_body'

			if user.mode == 'nature':
				c.execute(f'SELECT * FROM myself_hard_nature  where id ="{user.nature_score}"')
				rows = c.fetchone()
				user.nature_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_myself_hard_nature_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_hard_nature_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_nature'



			if user.mode == 'emodji':
				c.execute(f'SELECT * FROM myself_hard_emotions_feelings where id ="{user.emodji_score}"')
				rows = c.fetchone()
				user.emodji_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_myself_hard_emotions_feelings_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_myself_hard_emotions_feelings_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_emodji'


			if user.mode == 'stuart':
				c.execute(f'SELECT * FROM prof_avia where id ="{user.stuart_score}"')
				rows = c.fetchone()
				user.stuart_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_prof_avia_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_prof_avia_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_stuart'

			if user.mode == 'economy':
				c.execute(f'SELECT * FROM prof_economy where id ="{user.economy_score}"')
				rows = c.fetchone()
				user.economy_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_prof_economy_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_prof_economy_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_economy'

			if user.mode == 'enginere':
				c.execute(f'SELECT * FROM prof_engineer where id ="{user.enginere_score}"')
				rows = c.fetchone()
				user.enginere_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_prof_engineer_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_prof_engineer_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_enginere'


			if user.mode == 'guide':
				c.execute(f'SELECT * FROM prof_gids where id ="{user.guide_score}"')
				rows = c.fetchone()
				user.guide_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_prof_gids_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_prof_gids_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_guide'

			if user.mode == 'prog':
				c.execute(f'SELECT * FROM prof_programmer where id ="{user.prog_score}"')
				rows = c.fetchone()
				user.prog_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_prof_programmer_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_prof_programmer_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_prog'

			if user.mode == 'sport':
				c.execute(f'SELECT * FROM prof_sport where id ="{user.sport_score}"')
				rows = c.fetchone()
				user.sport_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_prof_sport_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_prof_sport_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_sport'

			if user.mode == 'place':
				c.execute(f'SELECT * FROM travel_local where id ="{user.place_score}"')
				rows = c.fetchone()
				user.place_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_travel_local_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_travel_local_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_place'

			if user.mode == 'dialog':
				c.execute(f'SELECT * FROM travel_about_myself where id ="{user.dialog_score}"')
				rows = c.fetchone()
				user.dialog_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_travel_about_myself_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_travel_about_myself_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_dialog'

			if user.mode == 'help':
				c.execute(f'SELECT * FROM travel_answer_for_help where id ="{user.help_score}"')
				rows = c.fetchone()
				user.help_score += 1
				massage = logic.request_in_massage(rows)
				if rows != None:
					bot_message = await message.answer(massage, reply_markup=kb5)
					bot_messages.append(bot_message.message_id)
					bot_messages.append(bot_message.message_id)
				else:  # Удалим все сообщения бота из списка по одному

					# Очистим список
					bot_messages.clear()

					await message.answer(text="Начинаем тест!")
					user.l = random.randint(0, (
							len(c.execute(f'SELECT * FROM test_travel_answer_for_help_0').fetchall()) - 1))

					c.execute(f'SELECT * FROM test_travel_answer_for_help_0 where id = {user.l}')
					rows = c.fetchone()
					rows = rows[:-1]
					rows2 = random.sample(rows[1:], len(rows[1:]))

					k = ReplyKeyboardMarkup(resize_keyboard=True)
					b1 = KeyboardButton(text=rows2[0])
					b2 = KeyboardButton(text=rows2[1])
					b3 = KeyboardButton(text=rows2[2])
					b4 = KeyboardButton(text=rows2[3])
					b5 = KeyboardButton(text='В главное меню')
					k.add(b1, b2, b3, b4, b5)

					await message.answer(text=f"Перевидите слово {rows[0]}", reply_markup=k)

					user.mode = '0_test_help'

@dp.message_handler(content_types=['text'])
async def test(message: types.Message):
	for user in users:
		if user.id == message.from_user.id:

			if message.text == 'Модуль1':
				if user.mode == 'myself':
					await message.answer(text='Выберите уровень', reply_markup=kb3)
					user.mode = 'modul1'
				if user.mode =='travel':
					await message.answer(text='Выберите категорию', reply_markup=kb13)
					user.mode = 'modul1'
				if user.mode =='prof':
					await message.answer(text='Выберите категорию', reply_markup=kb14)
					user.mode = 'modul1'

			if message.text == 'Модуль2':
				if user.mode == 'myself':
					await message.answer(text='Выберите уровень', reply_markup=kb3)
					user.mode = 'modul2'
				if user.mode =='travel':
					await message.answer(text='Выберите категорию', reply_markup=kb13)
					user.mode = 'modul2'
				if user.mode =='prof':
					await message.answer(text='Выберите категорию', reply_markup=kb14)
					user.mode = 'modul2'

			if message.text == 'Модуль3':
				if user.mode =='myself':
					await message.answer(text='Выберите уровень', reply_markup=kb3)
					user.mode = 'modul3'
				if user.mode =='travel':
					await message.answer(text='Выберите категорию', reply_markup=kb13)
					user.mode = 'modul3'
				if user.mode =='prof':
					await message.answer(text='Выберите категорию', reply_markup=kb14)
					user.mode = 'modul3'

			if message.text == 'В главное меню':
				user.mode = None
				await message.answer(text='Вы в главном меню', reply_markup=kb2)

			if user.mode =='test_animal':
				c.execute(f'SELECT * FROM test_myself_basic_animals where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_animal':
				c.execute(f'SELECT * FROM test_myself_basic_animals_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:
					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_animal_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_basic_animal").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_basic_animal").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_basic_animal").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_basic_animal").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							await message.answer(text='Все примеры были решены')
							await message.answer(text='Вы в главном меню', reply_markup=kb2)
							user.i = 0
							user.mode = None
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_dialog':
				c.execute(f'SELECT * FROM test_travel_about_myself where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_dialog':
				c.execute(f'SELECT * FROM test_travel_about_myself_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:
					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_dialog_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM travel_about_myself").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM travel_about_myself").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM travel_about_myself").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM travel_about_myself").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							await message.answer(text='Все примеры были решены')
							await message.answer(text='Вы в главном меню', reply_markup=kb2)
							user.i = 0
							user.mode = None
				else:
					await message.answer(text='Не верно')


			if user.mode =='test_communication':
				c.execute(f'SELECT * FROM test_myself_basic_communication where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_communication':
				c.execute(f'SELECT * FROM test_myself_basic_communication_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:
					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_communication_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_basic_communication").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_basic_communication").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_basic_communication").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_basic_communication").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							await message.answer(text='Все примеры были решены')
							await message.answer(text='Вы в главном меню', reply_markup=kb2)
							user.i = 0
							user.mode = None
				else:
					await message.answer(text='Не верно')


			if user.mode =='test_colorandnumer':
				c.execute(f'SELECT * FROM test_myself_basic_colorandnumer where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_colorandnumer':
				c.execute(f'SELECT * FROM test_myself_basic_colorandnumer_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_colorandnumer_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_basic_colorandnumer").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_basic_colorandnumer").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_basic_colorandnumer").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_basic_colorandnumer").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							await message.answer(text='Все примеры были решены')
							await message.answer(text='Вы в главном меню', reply_markup=kb2)
							user.i = 0
							user.mode = None
				else:
					await message.answer(text='Не верно')


			if user.mode =='test_eat':
				c.execute(f'SELECT * FROM test_myself_basic_eat where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_eat':
				c.execute(f'SELECT * FROM test_myself_basic_eat_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_eat_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_basic_eat").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_basic_eat").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_basic_eat").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_basic_eat").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							await message.answer(text='Все примеры были решены')
							await message.answer(text='Вы в главном меню', reply_markup=kb2)
							user.i = 0
							user.mode = None
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_transport':
				c.execute(f'SELECT * FROM test_myself_medium_transport where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_transport':
				c.execute(f'SELECT * FROM test_myself_medium_transport_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_transport_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_medium_transport").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_medium_transport").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_medium_transport").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_medium_transport").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							await message.answer(text='Все примеры были решены')
							await message.answer(text='Вы в главном меню', reply_markup=kb2)
							user.i = 0
							user.mode = None
				else:
					await message.answer(text='Не верно')


			if user.mode =='test_hobbies':
				c.execute(f'SELECT * FROM test_myself_medium_hobbies where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_hobbies':
				c.execute(f'SELECT * FROM test_myself_medium_hobbies_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_hobbies_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_medium_hobbies").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_medium_hobbies").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_medium_hobbies").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_medium_hobbies").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							await message.answer(text='Все примеры были решены')
							await message.answer(text='Вы в главном меню', reply_markup=kb2)
							user.i = 0
							user.mode = None
				else:
					await message.answer(text='Не верно')


			if user.mode =='test_family':
				c.execute(f'SELECT * FROM test_myself_medium_family where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_family':
				c.execute(f'SELECT * FROM test_myself_medium_family_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_family_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM test_myself_medium_family").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM test_myself_medium_family").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM test_myself_medium_family").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM test_myself_medium_family").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							await message.answer(text='Все примеры были решены')
							await message.answer(text='Вы в главном меню', reply_markup=kb2)
							user.i = 0
							user.mode = None
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_clothes':
				c.execute(f'SELECT * FROM test_myself_medium_clothes where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_clothes':
				c.execute(f'SELECT * FROM test_myself_medium_clothes_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_clothes_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_medium_clothes").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_medium_clothes").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_medium_clothes").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_medium_clothes").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							await message.answer(text='Все примеры были решены')
							await message.answer(text='Вы в главном меню', reply_markup=kb2)
							user.i = 0
							user.mode = None
				else:
					await message.answer(text='Не верно')
			if user.mode =='test_body':
				c.execute(f'SELECT * FROM test_myself_hard_body where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_body':
				c.execute(f'SELECT * FROM test_myself_hard_body_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_body_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_hard_body").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_hard_body").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_hard_body").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_hard_body").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_nature':
				c.execute(f'SELECT * FROM test_myself_hard_nature where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_nature':
				c.execute(f'SELECT * FROM test_myself_hard_nature_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_nature_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_hard_nature").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_hard_nature").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_hard_nature").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_hard_nature").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')


			if user.mode =='test_emodji':
				c.execute(f'SELECT * FROM test_myself_hard_emotions_feelings where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_emodji':
				c.execute(f'SELECT * FROM test_myself_hard_emotions_feelings_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_emodji_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM myself_hard_emotions_feelings").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM myself_hard_emotions_feelings").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM myself_hard_emotions_feelings").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM myself_hard_emotions_feelings").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_stuart':
				c.execute(f'SELECT * FROM test_prof_avia where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_stuart':
				c.execute(f'SELECT * FROM test_prof_avia_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_stuart_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM prof_avia").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM prof_avia").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM prof_avia").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM prof_avia").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_economy':
				c.execute(f'SELECT * FROM test_prof_economy where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_economy':
				c.execute(f'SELECT * FROM test_prof_economy_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_economy_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM prof_economy").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM prof_economy").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM prof_economy").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM prof_economy").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_enginere':
				c.execute(f'SELECT * FROM test_prof_engineer where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_enginere':
				c.execute(f'SELECT * FROM test_prof_engineer_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_enginere_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM prof_engineer").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM prof_engineer").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM prof_engineer").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM prof_engineer").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_guide':
				c.execute(f'SELECT * FROM test_prof_gids where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_guide':
				c.execute(f'SELECT * FROM test_prof_gids_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_guide_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM prof_gids").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM prof_gids").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM prof_gids").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM prof_gids").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')


			if user.mode =='test_prog':
				c.execute(f'SELECT * FROM test_prof_programmer where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_prog':
				c.execute(f'SELECT * FROM test_prof_programmer_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_prog_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM prof_programmer").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM prof_programmer").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM prof_programmer").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM prof_programmer").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_sport':
				c.execute(f'SELECT * FROM test_prof_sport where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_sport':
				c.execute(f'SELECT * FROM test_prof_sport_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_sport_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM prof_sport").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM prof_sport").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM prof_sport").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM prof_sport").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')

			if user.mode =='test_place':
				c.execute(f'SELECT * FROM test_travel_local where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_place':
				c.execute(f'SELECT * FROM test_travel_local_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_place_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM travel_local").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM travel_local").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM travel_local").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM travel_local").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')


			if user.mode =='test_help':
				c.execute(f'SELECT * FROM test_travel_answer_for_help where id = {str(user.l)}')
				rows = c.fetchone()
				rows = rows[:-1]
				if message.text == rows[user.i]:
					user.i+=1
					await message.answer(text ='Верно')
				else:
					await message.answer(text='Не угадали')
				if user.i == len(rows):
					user.i = 0
					await message.answer(text='Вы в главном меню', reply_markup=kb2)
					user.mode = None
			if user.mode =='0_test_help':
				c.execute(f'SELECT * FROM test_travel_answer_for_help_0 where id = {user.l}')
				rows = c.fetchone()
				rows = rows[:-1]

				if message.text == rows[1]:

					await message.answer(text='Верно', reply_markup=kb2)
					user.mode = None
				else:
					await message.answer(text='Не угадали')
			if user.mode == 'test_help_1':
				kb = ReplyKeyboardMarkup(resize_keyboard=True)
				b_menu = KeyboardButton(text="В главное меню")
				kb.add(b_menu)
				if message.text == c.execute("SELECT * FROM travel_answer_for_help").fetchall()[user.i][1]:
					if user.i != (len(c.execute("SELECT * FROM travel_answer_for_help").fetchall())):
						await message.answer(text='Верно')
						user.i+=1
						if user.i != (len(c.execute("SELECT * FROM travel_answer_for_help").fetchall())):
							await message.answer(
							text=f'Набирите слово {c.execute("SELECT * FROM travel_answer_for_help").fetchall()[user.i][2]}',
							reply_markup=kb)
						else:
							user.i = 0
				else:
					await message.answer(text='Не верно')
current_word_index = 0
words = []

if __name__ == "__main__":
	executor.start_polling(dp)
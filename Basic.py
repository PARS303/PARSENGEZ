from aiogram import types

from kb import kb5


async def handle_basic_level(message: types.Message):
	c.execute('SELECT * FROM myself_basic_communication')
	rows = c.fetchall()
	for row in rows:
		# Сохраним идентификатор каждого сообщения бота в список
		bot_message = await message.answer(row, reply_markup=kb5)
		bot_messages.append(bot_message.message_id)



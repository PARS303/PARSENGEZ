import aiogram
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text="Погнали!")
kb.add(b1)

kb2 = ReplyKeyboardMarkup(resize_keyboard=True)
b2 = KeyboardButton(text="Для себя")
b13 = KeyboardButton(text="Для путешествия")
b14 = KeyboardButton(text="Для профессии")
kb2.add(b2,b13,b14)

kb3 = ReplyKeyboardMarkup(resize_keyboard=True)
b5 = KeyboardButton(text="Базовый")
b6 = KeyboardButton(text="Средний")
b7 = KeyboardButton(text="Профессиональный")
kb3.add(b5,b6,b7)

kb4 = ReplyKeyboardMarkup(resize_keyboard=True)
b8 = KeyboardButton(text="Общение")
b9 = KeyboardButton(text="Еда")
b10 = KeyboardButton(text="Животные")
b11 = KeyboardButton(text="Цвета и цифры")
kb4.add(b8,b9,b10,b11)

kb5 = ReplyKeyboardMarkup(resize_keyboard=True)
b12 = KeyboardButton(text="Я запомнил. Дальше!")
b_menu = KeyboardButton(text="В главное меню")
kb5.add(b12, b_menu)

kb6 = ReplyKeyboardMarkup(resize_keyboard=True)
b15 = KeyboardButton(text="Пройти тест!")
kb6.add(b15)

kb7 = ReplyKeyboardMarkup(resize_keyboard=True)
b17 = KeyboardButton(text="Дома")
b18 = KeyboardButton(text="Особняки")
b19 = KeyboardButton(text="Квартиры")
kb7.add(b17,b18,b19)

kb8 = ReplyKeyboardMarkup(resize_keyboard=True)
b20 = KeyboardButton(text="Унитаз")
b21 = KeyboardButton(text="Собака")
b22 = KeyboardButton(text="Мама Андрея")
kb8.add(b20,b21,b22)

kb9 = ReplyKeyboardMarkup(resize_keyboard=True)
b23 = KeyboardButton(text="Папа андрея!?")
b24 = KeyboardButton(text="СКатЕртЬ")
b25 = KeyboardButton(text="Кошка")
kb9.add(b23,b24,b25)

kb10 = ReplyKeyboardMarkup(resize_keyboard=True)
b26 = KeyboardButton(text="Общение")
b27 = KeyboardButton(text="Еда")
b28 = KeyboardButton(text="Цвета")
b29 = KeyboardButton(text="Животные")
kb10.add(b26,b27,b28,b29)

kb11 = ReplyKeyboardMarkup(resize_keyboard=True)
b30 = KeyboardButton(text="Одежда")
b31 = KeyboardButton(text="Семья")
b32 = KeyboardButton(text="Хобби")
b33 = KeyboardButton(text="Транспорт")
kb11.add(b30,b31,b32,b33)

kb12 = ReplyKeyboardMarkup(resize_keyboard=True)
b34 = KeyboardButton(text="Эмоции")
b35 = KeyboardButton(text="Тело")
b36 = KeyboardButton(text="Природа")
kb12.add(b34,b35,b36)
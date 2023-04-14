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
b_menu = KeyboardButton(text="В главное меню")
kb3.add(b5,b6,b7,b_menu)

kb4 = ReplyKeyboardMarkup(resize_keyboard=True)
b8 = KeyboardButton(text="Общение")
b9 = KeyboardButton(text="Еда")
b10 = KeyboardButton(text="Животные")
b11 = KeyboardButton(text="Цвета и цифры")
kb4.add(b8,b9,b10,b11)

kb5 = ReplyKeyboardMarkup(resize_keyboard=True)
b12 = KeyboardButton(text="Я запомнил. Дальше!")
kb5.add(b12, b_menu)

kb10 = ReplyKeyboardMarkup(resize_keyboard=True)
b26 = KeyboardButton(text="Общение")
b27 = KeyboardButton(text="Еда")
b28 = KeyboardButton(text="Цвета")
b29 = KeyboardButton(text="Животные")
kb10.add(b26,b27,b28,b29,b_menu)

kb11 = ReplyKeyboardMarkup(resize_keyboard=True)
b30 = KeyboardButton(text="Одежда")
b31 = KeyboardButton(text="Семья")
b32 = KeyboardButton(text="Хобби")
b33 = KeyboardButton(text="Транспорт")
kb11.add(b30,b31,b32,b33,b_menu)

kb12 = ReplyKeyboardMarkup(resize_keyboard=True)
b34 = KeyboardButton(text="Эмоции")
b35 = KeyboardButton(text="Тело")
b36 = KeyboardButton(text="Природа")
kb12.add(b34,b35,b36,b_menu)

kb13 = ReplyKeyboardMarkup(resize_keyboard=True)
b37 = KeyboardButton(text="Диалог")
b38 = KeyboardButton(text="Вопросы для помощи")
b39 = KeyboardButton(text="Места")
kb13.add(b37,b38,b39,b_menu)

kb14 = ReplyKeyboardMarkup(resize_keyboard=True)
b40 = KeyboardButton(text="Спорт")
b41 = KeyboardButton(text="Программирование")
b42 = KeyboardButton(text="Гид")
b43 = KeyboardButton(text="Инженер")
b44 = KeyboardButton(text="Экономист")
b45 = KeyboardButton(text="Стюарт")
kb14.add(b40,b41,b42,b43,b44,b45,b_menu)

kb15 = ReplyKeyboardMarkup(resize_keyboard=True)
b46 = KeyboardButton(text="Модуль1")
b47 = KeyboardButton(text="Модуль2")
b48 = KeyboardButton(text="Модуль3")
kb15.add(b46,b47,b48,b_menu)
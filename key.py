from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton

def starting():
	menu = ReplyKeyboardMarkup(resize_keyboard=True)
	num1 = KeyboardButton('Создать из цвета')
	num2 = KeyboardButton('Создать из шаблона')
	menu.add(num1,num2)
	return menu

def tamplate():
	menu = ReplyKeyboardMarkup(resize_keyboard=True)
	num1 = KeyboardButton('Загрузить своё изображение')
	num2 = KeyboardButton('Выбрать из предлоежнных')
	menu.add(num1).add(num2)
	return menu


def choose_color_icon(arg):
	menu = InlineKeyboardMarkup(resize_keyboard=True)
	num1 = InlineKeyboardButton(text= 'Выбрать', callback_data='choose_color_icon_' + str(arg))
	menu.add(num1)
	return menu


	
def choose_icon(arg):
	menu = InlineKeyboardMarkup(resize_keyboard=True)
	num1 = InlineKeyboardButton(text= 'Выбрать', callback_data='choose_icon_' + str(arg))
	menu.add(num1)
	return menu

def colors():
	menu = InlineKeyboardMarkup(resize_keyboard=True)
	num1 = InlineKeyboardButton(text= 'Красные тона', callback_data='color_red')
	num2 = InlineKeyboardButton(text= 'Зелёные тона', callback_data='color_green')
	num3 = InlineKeyboardButton(text= 'Розовые тона', callback_data='color_')
	num4 = InlineKeyboardButton(text= 'Оранжевые тона', callback_data='color_')
	num5 = InlineKeyboardButton(text= 'Жёлтые тона', callback_data='color_')
	num6 = InlineKeyboardButton(text= 'Синие тона', callback_data='color_')
	num6 = InlineKeyboardButton(text= 'Фиолетовые тона', callback_data='color_')
	num6 = InlineKeyboardButton(text= 'Белые тона', callback_data='color_')
	num6 = InlineKeyboardButton(text= 'Коричневые тона', callback_data='color_')
	num6 = InlineKeyboardButton(text= 'Основные цвета', callback_data='color_')
	num6 = InlineKeyboardButton(text= 'Серые тона', callback_data='color_')
	menu.add(num1,num2,num3).add(num4,num5,num6)
	return menu

def set_color(arg, color_list):
	menu = InlineKeyboardMarkup(resize_keyboard=True)
	if arg+1 == 3:
		num1 = InlineKeyboardButton(text= '1', callback_data='set_color_'+str(color_list[0]))
		num2 = InlineKeyboardButton(text= '2', callback_data='set_color_'+str(color_list[1]))
		num3 = InlineKeyboardButton(text= '3', callback_data='set_color_'+str(color_list[2]))
	else:
		num1 = InlineKeyboardButton(text= '4', callback_data='set_color_'+str(color_list[3]))
		num2 = InlineKeyboardButton(text= '5', callback_data='set_color_'+str(color_list[4]))
		num3 = InlineKeyboardButton(text= '6', callback_data='set_color_'+str(color_list[5]))
	menu.add(num1,num2,num3)
	return menu
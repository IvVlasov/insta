from aiogram import  executor, types
from config import bot, dp, TOKEN
from datetime import datetime, date, time
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup,KeyboardButton

import logging 
import key
import main
import requests
from PIL import Image
from io import BytesIO


logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands=['start'])
async def echo(message:types.Message):
    await message.answer("Хотите создать свою хайлайт для инста?", reply_markup = key.starting())



@dp.message_handler(text=['Создать из цвета'])
async def echo(message:types.Message):
	await message.answer("Введите цвет в формате rgb (напирмер 255,255,255) или выберите какого тона цвет использовать", reply_markup = key.colors())



@dp.message_handler(text=['Создать из шаблона'])
async def echo(message:types.Message):
	await message.answer("Какой шаблон вы хотите использовать?", reply_markup= key.tamplate())
	



@dp.callback_query_handler(lambda c: c.data.startswith('color_'))
async def colors(call):
	await bot.delete_message(call.message.chat.id, call.message.message_id)
	await ColorForm.back.set()
	color = call.data.split('_')[1]
	if color == 'red':
		rgb_list = [(205, 92, 92), (240, 128, 128),(250, 128, 114), (233, 150, 122), (255, 160, 122), (220, 20, 60)]
	if color == 'green':
		rgb_list = [(173, 255, 47), (50, 205, 50),(34, 139, 34),(0, 100, 0),(144, 238, 144),(127, 255, 0)]

	new_im = Image.new('RGB', (900, 300))
	x_offset = 0
	
	for i, el in enumerate(rgb_list):

		new_im.paste(main.colorImage(el), (x_offset,0))
		x_offset += 300

		if (i+1) % 3 == 0:
			with BytesIO() as output:
			    new_im.save(output, format="PNG")
			    contents = output.getvalue()

			await bot.send_photo(call.message.chat.id, photo = contents,reply_markup = key.set_color(i,rgb_list))

			new_im = Image.new('RGB', (900, 300))
			x_offset = 0 

			continue





@dp.message_handler(text=['Загрузить своё изображение'])
async def echo(message:types.Message):
	await message.answer("Загрузите своё изображение (720x1280)")
	await Form.photo.set()





#### States #####

class Form(StatesGroup):
    photo = State()  
    icon = State()  

class ColorForm(StatesGroup):
    back = State()  
    icon = State()  

@dp.message_handler(content_types =['photo'] , state=Form.photo)
async def process_photo(message: types.Message, state: FSMContext):
    file = await bot.get_file(message.photo[-1].file_id)
    await state.update_data(photo=file.file_path)
    await Form.next()
    await message.reply('asd')
    for i in range(6):
    	if i == 0 :
    		continue
    	path = 'icons/Mini/' + str(i) + '.png'
    	await bot.send_photo(message.chat.id,photo=open(path, 'rb'), reply_markup = key.choose_icon(i))


@dp.callback_query_handler(lambda c: c.data.startswith('choose_icon_'), state=Form.icon)
async def save_anket(call, state: FSMContext):
	arg = call.data.split('_')[2]
	await state.update_data(icon = 'icons/'+ str(arg)+ '.png')
	async with state.proxy() as data:
		r = requests.get('https://api.telegram.org/file/bot' + TOKEN+ '/'+data['photo'])
		await bot.send_photo(call.message.chat.id, photo = main.createBackground(r,  data['icon']))
	await state.finish()




@dp.callback_query_handler(lambda c: c.data.startswith('set_color'), state=ColorForm.back)
async def colors(call, state: FSMContext):
	color = call.data.split('_')[2]
	try:
		await bot.delete_message(call.message.chat.id, call.message.message_id)
		await bot.delete_message(call.message.chat.id, call.message.message_id-1)
	except:
		pass
	await ColorForm.next()

	await bot.send_photo(call.message.chat.id, photo = main.color_back(color))
	await state.update_data(back = color)

	for i in range(6):
		if i == 0 :
			continue
		path = 'icons/Mini/' + str(i) + '.png'
		await bot.send_photo(call.message.chat.id,photo=open(path, 'rb'), reply_markup = key.choose_color_icon(i))


@dp.callback_query_handler(lambda c: c.data.startswith('choose_color_icon_'), state=ColorForm.icon)
async def save_anket(call, state: FSMContext):
	arg = call.data.split('_')[3]
	for i in range(int(arg)):
		await bot.delete_message(call.message.chat.id, call.message.message_id-i)
		try: 
			await bot.delete_message(call.message.chat.id, call.message.message_id+i)
		except:
			pass

	await state.update_data(icon = 'icons/'+ str(arg)+ '.png')

	async with state.proxy() as data:
		await bot.send_photo(call.message.chat.id, photo = main.create_color_Background(data['back'],  data['icon']))
	await state.finish()




if __name__ == "__main__":
	executor.start_polling(dp, skip_updates=True)
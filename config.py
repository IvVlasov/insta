
from aiogram import  Bot , Dispatcher 
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Токен телеграм бота, получается у BotFather

TOKEN = "botTOken"



# Создание диспатчера
bot = Bot(token=TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)




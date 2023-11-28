from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='6479180128:AAGOfpLH50y9ne0FgfcQS_JhAaH5Fj87rH8')

dp = Dispatcher(bot, storage=storage)

from aiogram import Bot, types
from aiogram import Dispatcher
from core.config import settings

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

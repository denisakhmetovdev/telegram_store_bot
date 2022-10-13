from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from os import getenv
from dotenv import load_dotenv
from pathlib import Path


config_path = Path(__file__).resolve().parent
dotenv_path = Path(config_path, '.env')

load_dotenv(dotenv_path)

bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(bot)

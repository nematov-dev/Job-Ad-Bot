import logging
from aiogram import Dispatcher,Bot

from data import config

# A bot object
bot = Bot(token=config.BOT_TOKEN)

# Create Dispatcher
db = Dispatcher()

# log settings
logging.basicConfig(level=logging.INFO)
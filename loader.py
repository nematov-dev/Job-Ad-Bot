import logging
from aiogram import Dispatcher,Bot

from data import config

# A bot object
bot = Bot(token="8028327839:AAFpD0RiQzPTZgmdCLoIn9R0y6KEIR2oodo")

# Create Dispatcher
db = Dispatcher()

# log settings
logging.basicConfig(level=logging.INFO)
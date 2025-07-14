from decouple import config

#bot
BOT_TOKEN = config("BOT_TOKEN")
BOT_USERNAME = config("BOT_USERNAME")
ADMIN_ID = config("ADMIN_ID")
CHANEL_ID = config("CHANEL_ID")
CHANEL_USERNAME = config("CHANEL_USERNAME")

#database
DB_NAME = config("DB_NAME")
DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS")
DB_HOST = config("DB_HOST")
DB_PORT = config("DB_PORT")
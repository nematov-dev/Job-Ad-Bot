import asyncio
import logging
from aiogram import Bot
from aiogram.types import BotCommand

import loader
from data import config
from database import queries
from handlears import user, admin

async def startup_answer(bot: Bot):
        await bot.send_message(config.ADMIN_ID, text="✅ Bot ishga tushdi!")

async def shutdown_answer(bot: Bot):
        await bot.send_message(config.ADMIN_ID, text="❌ Bot to'xtatildi!")

async def main():
    # log settings
    logging.basicConfig(level=logging.INFO)

    # Create Tables
    queries.create_users_table()
    queries.create_worker_ads_table()

    # Startup and Shutdown 
    loader.db.startup.register(startup_answer)
    loader.db.shutdown.register(shutdown_answer)

    # Routers
    loader.db.include_router(user.router)
    # loader.db.include_router(admin.router)

    # Bot commands
    await loader.bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushurish"),
        BotCommand(command="/help", description="Bot haqida batafsil"),
        BotCommand(command="/add_worker", description="Xodim kerak e'loni joylash"),
        BotCommand(command="/add_job", description="Ish kerak e'loni joylash"),
        BotCommand(command='/cancel',description="Jarayoni bekor qilish"),
        BotCommand(command='/search',description="Ish qidirish"),
        BotCommand(command="/my_ads", description="Mening e'lonlarim"),
    ])

    # Run the bot
    try:
        await loader.db.start_polling(loader.bot)
    finally:
        await loader.bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())

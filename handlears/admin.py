from datetime import datetime
from aiogram import F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from filters.is_admin import IsAdmin
from keyboards.admin_keyboard import main_keyboard_admin
from database import queries
from data.config import BOT_USERNAME


router = Router()

# /admin Command answer
@router.message(IsAdmin(), Command("admin"))
async def admin_start(message: Message):
    await message.answer(f"<b>Asslomu alaykum admin: {message.from_user.full_name} !</b>\n\nMarhamat o'zingizga kerakli tugmalardan foydalaning 👇🏻",reply_markup=main_keyboard_admin(),parse_mode="HTML")

# stat Command answer
@router.message(IsAdmin(), F.text == "📊 Statistika")
async def admin_start(message: Message):
    # User stat
    users_all_count = queries.stat_user_count()
    users_today_count = queries.stat_user_today()
    users_7days_count = queries.stat_user_7day()
    users_1month = queries.stat_user_month()
    
    # Worker ads stat
    worker_ads_all_count = queries.stat_worker_ads_count()
    worker_ads_active = queries.stat_worker_ads_active_count()
    worker_ads_deactive = queries.stat_worker_ads_deactive_count()

    # Job ads stat
    job_ads_all_count = queries.stat_job_ads_count()

    # Date Time
    now = datetime.now()

    today_date = now.strftime("%Y-%m-%d")
    current_time = now.strftime("%H:%M")

    # Statistika javobi
    await message.answer(
    f"""📊 <b>@{BOT_USERNAME} bot statistikasi</b>:

👤 <b>Foydalanuvchilar:</b>
• Barcha foydalanuvchilar soni: <b>{users_all_count}</b>
• Bugun qo‘shilgan foydalanuvchilar: <b>{users_today_count}</b>
• Oxirgi 7 kun ichida qo‘shilgan: <b>{users_7days_count}</b>
• Oxirgi 1 oy ichida qo‘shilgan: <b>{users_1month}</b>

🏢 <b>Ishchi kerak e’lonlari:</b>
• Umumiy e’lonlar soni: <b>{worker_ads_all_count}</b>
• Faol e’lonlar: <b>{worker_ads_active}</b>
• Faolsizlantirilgan e’lonlar: <b>{worker_ads_deactive}</b>

👤 <b>Ish izlovchilar e’lonlari:</b>
• Umumiy e’lonlar soni: <b>{job_ads_all_count}</b>

🕓 <i>Statistika yangilangan vaqti: {today_date} | {current_time}</i>
""",
    reply_markup=main_keyboard_admin(),
    parse_mode="HTML"
)

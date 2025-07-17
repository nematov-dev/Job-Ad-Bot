import re
from aiogram import Router, F,Bot
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.types import CallbackQuery


from keyboards.user_keyboard import main_keyboard,coniform_keyboard,cancel_keyboard,ad_deactivate_keyboard
from keyboards.admin_keyboard import confirm_inline_worker,confirm_inline_job
from states import user_state
from data.config import ADMIN_ID,CHANEL_ID,CHANEL_USERNAME,BOT_USERNAME
from database import queries

router = Router()

# Start command answer

@router.message(Command("start"))
async def start(message: Message):
    user = message.from_user
    if not queries.check_id(user.id,): #check if the user is not in the database
       queries.add_user(telegram_id=user.id, name=user.first_name, surname=user.last_name,username=user.username) # database add user

    text = f"""<b>👋🏻 Assalomu alaykum, {message.from_user.mention_html(message.from_user.full_name)} !\n</b>
🤖 Sizni botimizda ko‘rganimizdan xursandmiz.\n
- Bu bot orqali:\n
<b>📌 Ish e’lonlarini joylashtirishingiz
📌 Mavjud ish e’lonlarini ko‘rishingiz,qidirishingiz
📌 E’lonlaringizni boshqarishingiz mumkin.\n</b>\n
Barcha e'lonlar: <a href='https://t.me/{CHANEL_USERNAME}'>Bu yerda </a>\n
❗Bot buyruqlari haqida ma’lumot olish uchun /help buyrug‘idan foydalaning.\n
<b>Marhamat, pasdagi tugmalardan foydalaning 👇🏻</b>"""

    await message.answer(text,parse_mode="HTML",reply_markup=main_keyboard())

# Help command answer

@router.message(Command("help"))
async def help(message: Message):
        text = f"""
🤖 <b>Bot haqida batafsil:</b>\n\nUshbu bot orqali siz e’lon berishingiz va mavjud e’lonlarni boshqarishingiz mumkin.\n
📌 <b>Asosiy buyruqlar:</b>\n
● /start — Botni ishga tushurish va ro‘yxatdan o‘tish.
● /help — Bot funksiyalari haqida ma’lumot.
● /add_worker - Xodim kerak e'loni joylash.
● /add_job - Ish kerak e'loni joylash.
● /cancel — Jarayondagi e’lonni bekor qilish.
● /my_ads — O‘zingiz joylashtirgan e’lonlarni ko‘rish.
● /search - E’lonlar orasidan ish qidirish.

📌 <b>Kanalimiz:</b> <a href='https://t.me/{CHANEL_USERNAME}'>Rasmiy kanal</a>

❗ <b>Eslatma:</b> E’lonlaringiz admin tasdig‘idan so‘ng kanalda e’lon qilinadi.

Marhamat, pasdagi tugmalardan foydalaning 👇🏻
    """
        await message.answer(text,parse_mode="HTML",reply_markup=main_keyboard())
        
# To the home page

@router.message(F.text == "↩️ Orqaga")
async def contact(message: Message):
    await message.answer("🏠 Bosh sahifa", parse_mode="HTML",reply_markup=main_keyboard())

# Add Worker answer

@router.message(F.text.in_({"🏢 Ishchi kerak","/add_worker"}))
async def ad_worker_start(message: Message,bot: Bot,state: FSMContext):
     await message.reply("<b>Ish nomini kiriting:</b> \n\nMasalan: Sotuvchi",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.worker_ad.name)

# Stop state 

@router.message(F.text.in_({"/cancel", "❌ Bekor qilish"}))
async def cancel(message: Message,bot: Bot,state: FSMContext):
     this_state = await state.get_state()
     if this_state is None:
          await message.reply("<b>Jarayoni bekor qilish uchun sizda e'lon mavjud emas.\n/start bosing.</b>",parse_mode="HTML")
     else: 
          await message.reply("<b>❎ Bekor qilindi!</b>",reply_markup=main_keyboard(),parse_mode="HTML")
          await state.clear()

# Start Worker Ad state

@router.message(user_state.worker_ad.name)
async def ad_worker_name(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(name=message.text)
     await message.reply("<b>Ish haqida qisqacha yozing:</b>\n\nMasalan: Kesh bozori 12b do'koniga xushmomila, chaqqon sotuvchi kerak.",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.worker_ad.description)

@router.message(user_state.worker_ad.description)
async def ad_worker_description(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(description=message.text)
     await message.reply("<b>Yosh chegarasini kiriting:</b>\n\nMasalan: 18-35",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.worker_ad.age)

@router.message(user_state.worker_ad.age)
async def ad_worker_age(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(age=message.text)
     await message.reply("<b>Ish vaqtini kiriting:</b>\n\nMasalan: 09:00-18:00",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.worker_ad.time)
    
@router.message(user_state.worker_ad.time)
async def ad_worker_time(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(time=message.text)
     await message.reply("<b>Hududni kiriting:</b>\n\nMasalan: Qashqadaryo viloyati,Shahrisabz Shahri",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.worker_ad.location)
    
@router.message(user_state.worker_ad.location)
async def ad_worker_location(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(location=message.text)
     await message.reply("<b>Maoshni kiriting:</b>\n\nMasalan: 2.000.000 so'm yoki Kelishamiz 🤝",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.worker_ad.price)

@router.message(user_state.worker_ad.price)
async def ad_worker_price(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(price=message.text)
     await message.reply("<b>Aloqa uchun telefon raqam yoki telegram username kiriting:</b>\n\nMasalan: @user",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.worker_ad.contact)
    
@router.message(user_state.worker_ad.contact)
async def ad_worker_contact(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(contact=message.text)
     data = await state.get_data()
     text = f"""
🏷 Holati: 🟢 Foal\n
🏢 <b>Ishchi kerak</b>\n
📌 <b>Ish nomi:</b> {data['name']}\n
📝 <b>Ish haqida:</b> {data['description']}\n
👤 <b>Yosh chegarasi:</b> {data['age']}\n
🕒 <b>Ish vaqti:</b> {data['time']}\n
📍 <b>Manzili:</b> {data['location']}\n
💰 <b>Maosh:</b> {data['price']}\n
📞 <b>Aloqa uchun:</b> {data['contact']}"""
     await message.answer_photo(photo="https://t.me/testimagesfor/6",caption=text,parse_mode="HTML")
     await message.reply("<b>❗Ma'lumotlaringizni tekshiring. E'loningizni tasdiqlaysizmi?</b>",parse_mode="HTML",reply_markup=coniform_keyboard())
     await state.set_state(user_state.worker_ad.coniform)

@router.message(user_state.worker_ad.coniform)
async def ad_worker_coniform(message: Message,bot: Bot,state: FSMContext):
     if message.text == "✅ Xa":
          data = await state.get_data()
          text = f"""
🏷 Holati: 🟢 Foal\n
🏢 <b>Ishchi kerak</b>\n
📌 <b>Ish nomi:</b> {data['name']}\n
📝 <b>Ish haqida:</b> {data['description']}\n
👤 <b>Yosh chegarasi:</b> {data['age']}\n
🕒 <b>Ish vaqti:</b> {data['time']}\n
📍 <b>Manzili: </b>{data['location']}\n
💰 <b>Maosh:</b> {data['price']}\n
📞 <b>Aloqa uchun:</b> {data['contact']}\n
<b>👉🏻 E'lon joylash uchun: @{BOT_USERNAME}</b>"""
          user_id = queries.get_user_id_by_telegram_id(message.from_user.id) # user database id

          if queries.create_worker_ad(user_id=user_id,name=data['name'],description=text): # database add worker ad
     
               await message.reply("👌")
               await message.reply(f"<b>🕐 E'longiz adminga muaffaqiyatli yuborildi!</b>\n\nAdmin tasdiqlashi bilan e'longiz guruhimizga joylanadi.\nGuruhimiz: @{CHANEL_USERNAME}",parse_mode="HTML",reply_markup=main_keyboard())
               await bot.send_photo(
                    chat_id=ADMIN_ID,
                    photo="https://t.me/testimagesfor/6",
                    caption=text,
                    reply_markup=confirm_inline_worker(user_id=message.from_user.id)
                    )
               await state.clear()
          else:
               await message.reply("❌ Xatolik, e'loningiz bekor qilindi!",reply_markup=main_keyboard())
          
     elif message.text == "❌ Yo'q":
          await message.reply("E'longiz bekor qilindi!",reply_markup=main_keyboard())
          await state.clear()
     else:
          await message.reply("Iltimos faqat `✅ Xa` yoki `❌ Yo'q` yuboring!")

# Stop Worker Ad state

# Admin Worker Ad coniform

@router.callback_query(F.data.startswith("confirm_worker:"))
async def on_confirm_worker(query: CallbackQuery, bot: Bot):
    _, user_id_str = query.data.split(':')
    user_id = int(user_id_str) # user telegram id
    db_user_id = queries.get_user_id_by_telegram_id(user_id) #user dabatase id

    await query.answer("✅ E’lon tasdiqlandi")
    await query.message.edit_reply_markup()
    await query.message.delete()

     # Channel send message
    send_msg = await bot.send_photo(
        chat_id=CHANEL_ID,
        photo="https://t.me/testimagesfor/6",
        caption=query.message.caption or "",
        parse_mode="HTML"
    )
    post_id = send_msg.message_id # channel message_id

     # Save chat_id and chat_message_id to database
    queries.add_chat_message_id_by_user_id(user_id=db_user_id,chat_message_id=post_id)

    # Foydalanuvchiga xabar
    await bot.send_message(user_id, f"✅ Sizning e’lon tasdiqlandi!\n\nhttps://t.me/{CHANEL_USERNAME}/{post_id}")

# Admin Worker Ad reject

@router.callback_query(F.data.startswith("reject_worker:"))
async def on_reject_worker(query: CallbackQuery, bot: Bot):
    _, telegram_id_str = query.data.split(':')
    telegram_id = int(telegram_id_str)
    user_id = queries.get_user_id_by_telegram_id(telegram_id)
    queries.del_worker_ad(user_id,) # database delete worker ad
    await query.answer("❌ E’lon bekor qilindi!") # send admin
    await query.message.edit_reply_markup()
    await query.message.delete()
    await bot.send_message(telegram_id, "❌ Admin e’loningizni rad etdi.") #send user


# Ad Job answer

@router.message(F.text.in_({"👤 Ish kerak","/add_job"}))
async def ad_job_start(message: Message,bot: Bot,state: FSMContext):
     await message.reply("<b>Ism Familiyangizni kiriting:</b> \n\nMasalan: Olim Olimov",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.job_ad.full_name)

# Start Job Ad state

@router.message(user_state.job_ad.full_name)
async def ad_job_name(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(full_name=message.text)
     await message.reply("<b>Yoshingizni kiriting:</b>\n\nMasalan: 20",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.job_ad.age)

@router.message(user_state.job_ad.age)
async def ad_job_age(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(age=message.text)
     await message.reply("<b>Kasbingizni kiriting:</b>\n\nMasalan: Sotuvchi",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.job_ad.job)

@router.message(user_state.job_ad.job)
async def ad_job_job(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(job=message.text)
     await message.reply("<b>O'zingiz haqida qisqacha yozing:</b>\n\nSotuv sohasida +3 yillik tajriba ega sotuvchiman",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.job_ad.description)
    
@router.message(user_state.job_ad.description)
async def ad_job_description(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(description=message.text)
     await message.reply("<b>Hududni kiriting:</b>\n\nMasalan: Qashqadaryo viloyati,Shahrisabz Shahri",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.job_ad.location)
    
@router.message(user_state.job_ad.location)
async def ad_job_location(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(location=message.text)
     await message.reply("<b>Aloqa uchun telefon raqam yoki telegram @username kiriting:</b>\n\nMasalan: @username",parse_mode="HTML",reply_markup=cancel_keyboard())
     await state.set_state(user_state.job_ad.contact)

@router.message(user_state.job_ad.contact)
async def ad_job_contact(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(contact=message.text)
     data = await state.get_data()
     text = f"""
📌 <b>Ish kerak</b>\n
👤 <b>Ism familiya:</b> {data['full_name']}\n
🕑 <b>Yosh:</b> {data['age']}\n
📂 <b>Kasb:</b> {data['job']}\n
🗒 <b>Batafsil:</b> {data['description']}\n
📍 <b>Hudud:</b> {data['location']}\n
📞 <b>Aloqa uchun:</b> {data['contact']}"""
     await message.answer_photo(photo="https://t.me/testimagesfor/7",caption=text,parse_mode="HTML")
     await message.reply("<b>❗Ma'lumotlaringizni tekshiring. E'loningizni tasdiqlaysizmi?</b>",parse_mode="HTML",reply_markup=coniform_keyboard())
     await state.set_state(user_state.job_ad.coniform)

@router.message(user_state.job_ad.coniform)
async def ad_job_coniform(message: Message,bot: Bot,state: FSMContext):
     if message.text == "✅ Xa":
          data = await state.get_data()
          text = f"""
📌 <b>Ish kerak</b>\n
👤 <b>Ism familiya:</b> {data['full_name']}\n
🕑 <b>Yosh:</b> {data['age']}\n
📂 <b>Kasb:</b> {data['job']}\n
🗒 <b>Batafsil:</b> {data['description']}\n
📍 <b>Hudud:</b> {data['location']}\n
📞 <b>Aloqa uchun:</b> {data['contact']}\n
<b>👉🏻 E'lon joylash uchun: @{BOT_USERNAME}</b>"""
          
          await message.reply("👌")
          await message.reply(f"<b>🕐 E'longiz adminga muaffaqiyatli yuborildi!</b>\n\nAdmin tasdiqlashi bilan e'longiz guruhimizga joylanadi.\nGuruhimiz: @{CHANEL_USERNAME}",parse_mode="HTML",reply_markup=main_keyboard())
          await bot.send_photo(
               chat_id=ADMIN_ID,
               photo="https://t.me/testimagesfor/7",
               caption=text,
               reply_markup=confirm_inline_job(user_id=message.from_user.id)
               )
          await state.clear()

     elif message.text == "❌ Yo'q":
          await message.reply("E'longiz bekor qilindi!",reply_markup=main_keyboard())
          await state.clear()
     else:
          await message.reply("Iltimos faqat `✅ Xa` yoki `❌ Yo'q` yuboring!")

# Admin Job Ad coniform

@router.callback_query(F.data.startswith("confirm_job:"))
async def on_confirm_job(query: CallbackQuery, bot: Bot):
    _, user_id_str = query.data.split(':')
    user_id = int(user_id_str) # user telegram id
    db_user_id = queries.get_user_id_by_telegram_id(user_id) #user dabatase id

    await query.answer("✅ E’lon tasdiqlandi")
    await query.message.edit_reply_markup()
    await query.message.delete()

     # Channel send message
    send_msg = await bot.send_photo(
        chat_id=CHANEL_ID,
        photo="https://t.me/testimagesfor/7",
        caption=query.message.caption or "",
        parse_mode="HTML"
    )
    post_id = send_msg.message_id # channel message_id

     # Create Job ad
    queries.create_job_ads(user_id=db_user_id,chat_message_id=post_id)

    # send message user
    await bot.send_message(user_id, f"✅ Sizning e’lon tasdiqlandi!\n\nhttps://t.me/{CHANEL_USERNAME}/{post_id}")

# Admin Job Ad reject

@router.callback_query(F.data.startswith("reject_job:"))
async def on_reject_job(query: CallbackQuery, bot: Bot):
    _, telegram_id_str = query.data.split(':')
    telegram_id = int(telegram_id_str)
    await query.answer("❌ E’lon bekor qilindi!") # send admin
    await query.message.edit_reply_markup()
    await query.message.delete()
    await bot.send_message(telegram_id, "❌ Admin e’loningizni rad etdi.") #send user

    
# Start My ads command

@router.message(F.text.in_({"📃 Mening e'lonlarim","/my_ads"}))
async def ad_worker_start(message: Message,bot: Bot):
     db_user_id = queries.get_user_id_by_telegram_id(message.from_user.id) # User database id
     worker_ads = queries.my_ads_worker(db_user_id) # all worker ads
     job_ads = queries.get_my_job_ads(db_user_id) # all job ads

     if worker_ads or job_ads: # Worker ads
          await message.reply("<b>Sizning mavjud faol e'lonlaringiz:</b>",parse_mode="HTML")
          for worker_ad in worker_ads:
               text = f"""<b>🆔 ID raqami: </b>{worker_ad[0]}\n
🏢 <b>Ishchi kerak</b>\n
🏷 Holati: {'🟢 Foal' if worker_ad[3] else '🔴 Foal emas' }\n
📌 <b>Ish nomi:</b> {worker_ad[2]}\n
➡️<b> Batafsil: t.me/{CHANEL_USERNAME}/{worker_ad[4]}</b>"""
               await message.reply(text,parse_mode="HTML",reply_markup=ad_deactivate_keyboard())
          for job_ad in job_ads: # Job ads
               text = f"""
📌 <b>Ish kerak\n\n➡️ Batafsil: t.me/{CHANEL_USERNAME}/{job_ad[2]}</b>"""
          await message.reply(text,parse_mode="HTML",reply_markup=ad_deactivate_keyboard())
               
     else:
          await message.reply("🤷🏻‍♂️ <b>Sizda birorta ham foal e'lon mavjud emas!\n\n➕ E'lon yaratish:\n/add_worker - Xodim kerak e'loni joylash.\n/add_job - Ish kerak e'loni joylash.</b>",parse_mode="HTML")

# Deactivate worker ad

@router.message(F.text == "🔴 E'loni foalsizlantirish")
async def worker_ad_deactive(message: Message,bot: Bot,state: FSMContext):
    await message.answer("<b>🆔 E'longiz ID raqamini kiriting: \n\n❗ Eslatma faqat 'Ishchi kerak' e'lonlaringizni foalsizlantirishingiz mumkin! </b>", parse_mode="HTML")
    await state.set_state(user_state.worker_ad_deactivate.worker_add_id)

# Deactivate worker ad id

@router.message(user_state.worker_ad_deactivate.worker_add_id)
async def worker_ad_deactive_id(message: Message,bot: Bot,state: FSMContext):
     await state.update_data(worker_ad_id=message.text)
     data = await state.get_data()
     db_user_id = queries.get_user_id_by_telegram_id(message.from_user.id) # user db id

     status = queries.update_worker_status_by_user_id(db_user_id, data['worker_ad_id']) # worker ad status
     if status:

          #send user message
          await message.answer("<b>👌 E'longiz foalsizlantirildi!</b>", parse_mode="HTML", reply_markup=main_keyboard())

          #channel edit message
          chat_message_id = queries.get_worker_ad_chat_message_id_by_id(data['worker_ad_id']) # message_id
          description = queries.get_worker_description_by_id(data['worker_ad_id'])[0] # description

          # New description:
          new_contact = re.sub(
          r"📞 <b>Aloqa uchun:</b> .*\n",
          "📞 <b>Aloqa uchun:</b> Mavjud emas\n",
          description
          )
          new_description = new_contact.replace("🏷 Holati: 🟢 Foal\n", "🏷 Holati: 🔴 Foal emas\n")

          await bot.edit_message_caption(
               chat_id=CHANEL_ID,
               message_id=chat_message_id[0],
               caption=f"{new_description}",
               parse_mode="HTML")

     else:
          await message.answer("<b>❗Bunday faol e'lon topilmadi yoki ID noto‘g‘ri!</b>", parse_mode="HTML")
     await state.clear()


# Search command answer

@router.message(F.text.in_({"🔍 Qidiruv","/search"}))
async def search_answer(message: Message,bot: Bot,state: FSMContext):
    await message.answer("<b>Marhamat qidirmoqchi bo'lgan ishingiz nomini kiriting: 👇🏻</b>", parse_mode="HTML",reply_markup=cancel_keyboard())
    await state.set_state(user_state.search.name)

# Search answer name state

@router.message(user_state.search.name)
async def search_answer_name(message: Message, bot: Bot, state: FSMContext):
     await state.update_data(name=message.text)
     data = await state.get_data()
     worker_ads = queries.search_worker_ad(name=data['name']) # worker ads

     if worker_ads:
          await message.reply("<b>🔍 Qidiruv natijalari: </b>",parse_mode="HTML")
          for worker_ad in worker_ads:
               text = f"""🏢 <b>Ishchi kerak</b>\n
🏷 Holati: {'🟢 Foal' if worker_ad[3] else '🔴 Foal emas' }\n
📌 <b>Ish nomi:</b> {worker_ad[2]}\n
➡️<b> Batafsil: t.me/{CHANEL_USERNAME}/{worker_ad[4]}</b>"""
               await message.reply(text,parse_mode="HTML")
     else:
          await message.reply("<b>🤷🏻‍♂️ Bunday ish topilmadi!</b>",parse_mode="HTML")


# Contact command answer

@router.message(F.text == "👨🏻‍💻 Murojat uchun")
async def contact(message: Message):
    text = """
📬 <b>Taklif, savol yoki murojaat uchun</b>:

✅ Bot administratori bilan quyidagi usulda bog‘lanishingiz mumkin:

👤 <b>Telegram:</b> <a href="t.me/N_saidakbar">Saidakbar Ne'matov</a>"""
    await message.answer(text, parse_mode="HTML")
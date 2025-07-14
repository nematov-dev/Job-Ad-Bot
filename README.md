# 👨‍💼 Telegram Ish Topish va E'lon Bot

Bu Telegram bot ish beruvchilar va ish qidiruvchilar uchun mo‘ljallangan.  
Foydalanuvchilar bot orqali ish joylari va ishchi e'lonlarini joylashlari, mavjud e'lonlarni ko‘rishlari va qidirish imkoniyatiga ega bo‘ladilar.  

Bot **aiogram** kutubxonasi yordamida ishlab chiqilgan.

---

## 📌 Bot buyruqlari

| Buyruq        | Tavsif                                          |
|:--------------|:------------------------------------------------|
| `/start`       | Botni ishga tushurish va asosiy menyuni ko‘rsatish |
| `/help`        | Bot haqida batafsil ma'lumot                     |
| `/add_worker`  | Ishchi kerakligi haqida e'lon joylash            |
| `/add_job`     | Ish kerakligi haqida e'lon joylash               |
| `/cancel`      | Hozirgi jarayonni bekor qilish                   |
| `/search`      | E'lonlarni qidirish                              |
| `/my_ads`      | Foydalanuvchining e'lonlarini ko‘rish            |

---

## 📦 O‘rnatish (Installation)

1. 📥 Repository’ni yuklab oling:

```bash
git clone https://github.com/nematov-dev/Job-Ad-Bot.git
cd Job-Ad-Bot
📦 Kerakli kutubxonalarni o‘rnating:


pip install -r requirements.txt
⚙️ .env faylini yaratib, quyidagilarni to‘ldiring:

BOT_TOKEN=your_bot_token
BOT_USERNAME=your_bot_username
ADMIN_ID=your_admin_id
CHANEL_ID=your_channel_id
CHANEL_USERNAME=your_channel_username
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASS=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port


🚀 Botni ishga tushirish:

python main.py


🛠 Texnologiyalar

Python 3.11+

Aiogram 3.x

PostgreSQL

Asyncio


📋 Foydalanish tartibi

Botni ishga tushiring va /start buyrug‘i orqali menyuga kiring.

Kerakli buyruqni tanlang:

Ish e'loni berish: /add_job

Ishchi kerakligi haqida e'lon berish: /add_worker

E’lonlaringizni ko‘rish: /my_ads

E’lonlarni qidirish: /search

Jarayonni istalgan vaqtda /cancel buyrug‘i orqali bekor qilishingiz mumkin.

/help buyrug‘i orqali barcha imkoniyatlar va bot haqida qo‘shimcha ma’lumot olishingiz mumkin.

📄 Litsenziya
Ushbu loyiha mualliflik huquqi bilan himoyalangan.
Loyihadan faqat muallif ruxsati bilan foydalanish mumkin.

📞 Muallif bilan bog‘lanish
👤 Muallif: Saidakbar Nematov – nematov.uz

📱 Telegram: @n_saidakbar

---
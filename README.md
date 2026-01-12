# 👨‍💼 Job Posting and Worker Search Telegram Bot

This Telegram bot is designed for **employers and job seekers**.  
Users can post job vacancies, search for available jobs, view their own ads, and explore other postings directly through Telegram.  

The bot is built using **Aiogram**, **PostgreSQL**, and **async Python**.

---

## 📌 Bot Commands

| Command        | Description                                        |
|:---------------|:--------------------------------------------------|
| `/start`       | Start the bot and show the main menu             |
| `/help`        | Show detailed information about the bot         |
| `/add_worker`  | Post an ad for needing a worker                  |
| `/add_job`     | Post a job ad for yourself                       |
| `/cancel`      | Cancel the current process                       |
| `/search`      | Search for job ads                               |
| `/my_ads`      | View your own job postings                       |

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/nematov-dev/Job-Ad-Bot.git
cd Job-Ad-Bot
```

2. **Install required dependencies:**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file in the project root and fill in your settings:**

```
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
```

---

## 🚀 Running the Bot

```bash
python main.py
```

The bot will connect to the PostgreSQL database and start listening for Telegram messages.

---

## 🛠 Technologies

- Python 3.11+
- Aiogram 3.x
- PostgreSQL
- Asyncio

---

## 📋 Usage Guide

1. Start the bot and enter the main menu using the **/start** command.
2. Choose the appropriate command:
   - Post a job ad: **/add_job**
   - Post a worker-needed ad: **/add_worker**
   - View your own ads: **/my_ads**
   - Search available ads: **/search**
3. You can cancel any ongoing process at any time using **/cancel**.
4. Use **/help** to get full information about the bot and its features.

---

## 👨‍💻 Developer

**[Saidakbar Ne'matov](https://nematov.uz)**

---

## 📄 License

This project is open-source and intended for free use and development.

---

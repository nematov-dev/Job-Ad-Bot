from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Main keyboard
def main_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🏢 Ishchi kerak"), KeyboardButton(text="👤 Ish kerak")],
            [KeyboardButton(text="📃 Mening e'lonlarim"),KeyboardButton(text="🔍 Qidiruv"), ],
            [KeyboardButton(text="👨🏻‍💻 Murojat uchun")]
        ],
        resize_keyboard=True
    )

# Coniform keyboard
def coniform_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ Xa"), KeyboardButton(text="❌ Yo'q")],
        ],
        resize_keyboard=True
    )

#Cancel keyboard
def cancel_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="❌ Bekor qilish")],
        ],
        resize_keyboard=True
    )

# Ad deactivate
def ad_deactivate_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🔴 E'loni foalsizlantirish")],
            [KeyboardButton(text="↩️ Orqaga")],

        ],
        resize_keyboard=True
    )
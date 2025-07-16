from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# admin coniform worker ad
def confirm_inline_worker(user_id: int):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"confirm_worker:{user_id}"),
            InlineKeyboardButton(text="❌ Rad etish", callback_data=f"reject_worker:{user_id}")
        ]
    ])
    return kb


# admin coniform job ad
def confirm_inline_job(user_id: int):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"confirm_job:{user_id}"),
            InlineKeyboardButton(text="❌ Rad etish", callback_data=f"reject_job:{user_id}")
        ]
    ])
    return kb


# Admin Main keyboard

def main_keyboard_admin():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📩 Xabar yuborish"), KeyboardButton(text="📊 Statistika")]
        ],
        resize_keyboard=True
    )

#Cancel keyboard
def cancel_keyboard_admin():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="❗ Bekor qilish")],
        ],
        resize_keyboard=True
    )
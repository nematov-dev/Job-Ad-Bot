from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

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
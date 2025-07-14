from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

# admin coniform ad
def confirm_inline(user_id: int):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data=f"confirm:{user_id}"),
            InlineKeyboardButton(text="❌ Rad etish", callback_data=f"reject:{user_id}")
        ]
    ])
    return kb
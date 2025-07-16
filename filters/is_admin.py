from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from data.config import ADMIN_ID 

class IsAdmin(BaseFilter):
    async def __call__(self, event: Message | CallbackQuery) -> bool:
        return event.from_user.id == int(ADMIN_ID)

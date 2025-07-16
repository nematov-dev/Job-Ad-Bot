from aiogram.fsm.state import StatesGroup,State

# Admin send message users state
class admin_message(StatesGroup):
    message = State()
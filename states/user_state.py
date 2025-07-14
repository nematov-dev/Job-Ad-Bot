from aiogram.fsm.state import State,StatesGroup

# Worker ad state

class worker_ad(StatesGroup):
    name = State()
    description = State()
    age = State()
    time = State()
    location = State()
    price = State()
    contact = State()
    coniform = State()

# Worker ad deactivate state

class worker_ad_deactivate(StatesGroup):
    worker_add_id = State()

# Worker ad search state

class search(StatesGroup):
    name = State()
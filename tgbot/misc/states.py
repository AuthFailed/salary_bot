from aiogram.fsm.state import StatesGroup, State


class SalaryCountStates(StatesGroup):
    HOURLY_RATE = State()
    HOURS_WORKED = State()
    AHT = State()
    FLR = State()
    GOK = State()
    CLIENT_RATING = State()

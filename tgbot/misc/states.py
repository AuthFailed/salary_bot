from aiogram.fsm.state import StatesGroup, State


class SalaryCountStates(StatesGroup):
    POSITION = State()
    HOURLY_RATE = State()
    HOURS_WORKED = State()
    COEFFICIENT = State()
    AHT = State()
    FLR = State()
    GOK = State()
    CLIENT_RATING = State()
    TESTS = State()
    SL = State()


class VacationCountStates(StatesGroup):
    TOTAL_YEAR_SALARY = State()
    VACATION_DAYS = State()

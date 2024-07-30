from aiogram.fsm.state import StatesGroup, State


class SalaryCountStates(StatesGroup):
    COUNT_TYPE = State()
    PREMIUM_PERCENT = State()
    POSITION = State()
    HOURLY_RATE = State()
    HOURS_WORKED = State()
    COEFFICIENT = State()
    AHT = State()
    FLR = State()
    GOK = State()
    CLIENT_RATING = State()
    TESTS = State()
    ACKNOWLEDGMENTS = State()
    MENTOR = State()
    MENTOR_TYPE = State()
    MENTOR_DAYS = State()
    SL = State()


class VacationCountStates(StatesGroup):
    TOTAL_YEAR_SALARY = State()
    VACATION_DAYS = State()

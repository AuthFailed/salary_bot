from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from tgbot.misc.states import VacationCountStates
from tgbot.misc.salary import vacation_pay

vacation_router = Router()


@vacation_router.callback_query(F.data == "count_vacation")
async def create_order(query: CallbackQuery, state: FSMContext):
    await query.answer(text="Вы выбрали расчет отпускных!")
    await state.set_state(VacationCountStates.TOTAL_YEAR_SALARY)

    await query.message.edit_text(
        "Давай посчитаем отпускные\n💸 Введи свою годовую зарплату\nВводить нужно сумму выплаченных на руки за последние 12 месяцев."
    )


@vacation_router.message(VacationCountStates.TOTAL_YEAR_SALARY)
async def process_total_year_salary(message: Message, state: FSMContext) -> None:
    await state.update_data(TOTAL_YEAR_SALARY=message.text)
    await state.set_state(VacationCountStates.VACATION_DAYS)

    await message.answer("📅 Теперь введи кол-во дней отпуска:")


@vacation_router.message(VacationCountStates.VACATION_DAYS)
async def process_coefficient(message: Message, state: FSMContext) -> None:
    await state.update_data(VACATION_DAYS=message.text)

    user_data = await state.get_data()
    vacation_payment = await vacation_pay(
        total_year_salary=float(user_data["TOTAL_YEAR_SALARY"].replace(",", ".")),
        vacation_days_count=int(user_data["VACATION_DAYS"]),
    )
    await message.answer(f"""
Спасибо! Вот расчет с введенными данными:
💸 <b>ЗП за год</b>: {user_data["TOTAL_YEAR_SALARY"]}
📅 <b>Дней отпуска</b>: {user_data["VACATION_DAYS"]}

За {user_data["VACATION_DAYS"]} дней отпуска ты получишь примерно {vacation_payment} руб""")
    await state.clear()

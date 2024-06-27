from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.formatting import as_section, as_key_value, as_marked_list
from aiogram.fsm.context import FSMContext

from tgbot.keyboards.inline import (
    salary_menu,
    position,
    salary_specialistist_aht,
    salary_supervisor_aht,
    OrderCallbackData,
    salary_specialistist_flr,
    salary_supervisor_flr,
    salary_specialistist_gok,
    salary_supervisor_gok,
    salary_specialist_rate,
    salary_specialist_tests,
    salary_supervisor_sl,
)
from tgbot.misc.states import SalaryCountStates
from tgbot.misc.salary import salary_with_percents

menu_router = Router()


@menu_router.message(Command("salary"))
async def show_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Выбери пункт меню:", reply_markup=salary_menu())


# We can use F.data filter to filter callback queries by data field from CallbackQuery object
@menu_router.callback_query(F.data == "count_salary")
async def create_order(query: CallbackQuery, state: FSMContext):
    await query.answer(text="Вы выбрали расчет ЗП!")
    await state.set_state(SalaryCountStates.POSITION)

    await query.message.edit_text(
        "Давай посчитаем зарплату\nВыбери свою должность", reply_markup=position()
    )


@menu_router.callback_query(F.data.contains("position"))
@menu_router.message(SalaryCountStates.POSITION)
async def process_position(query: CallbackQuery, state: FSMContext) -> None:
    await state.update_data(POSITION=query.data.split("_")[-1])
    await state.set_state(SalaryCountStates.HOURLY_RATE)

    await query.message.edit_text(
        "Давай посчитаем зарплату\nВведи часовую ставку в чат"
    )


@menu_router.message(SalaryCountStates.HOURLY_RATE)
async def process_hourly_rate(message: Message, state: FSMContext) -> None:
    hourly_rate_formatted = message.text.replace(",", ".")
    await state.update_data(HOURLY_RATE=hourly_rate_formatted)
    await state.set_state(SalaryCountStates.HOURS_WORKED)
    await message.answer("⏳ Теперь введи <b>кол-во отработанных часов</b>")


@menu_router.message(SalaryCountStates.HOURS_WORKED)
async def process_hours_worked(message: Message, state: FSMContext) -> None:
    await state.update_data(HOURS_WORKED=message.text)
    await state.set_state(SalaryCountStates.AHT)

    user_data = await state.get_data()
    if user_data["POSITION"] == "specialist":
        await message.answer(
            "⚡ Введи процент премии за <b>AHT</b>",
            reply_markup=salary_specialistist_aht(),
        )
    else:
        await message.answer(
            "⚡ Введи процент премии за <b>AHT</b>",
            reply_markup=salary_supervisor_aht(),
        )


@menu_router.callback_query(F.data.contains("aht"))
@menu_router.message(SalaryCountStates.AHT)
async def process_aht(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer(text=f"Процент премии за AHT - {query.data.split("_")[-1]}!")
    await state.update_data(AHT=query.data.split("_")[-1])
    await state.set_state(SalaryCountStates.FLR)

    user_data = await state.get_data()
    if user_data["POSITION"] == "specialist":
        await query.message.edit_text(
            "⚙️ Теперь выбери процент премии за <b>FLR</b>",
            reply_markup=salary_specialistist_flr(),
        )
    else:
        await query.message.edit_text(
            "⚙️ Теперь выбери процент премии за <b>FLR</b>",
            reply_markup=salary_supervisor_flr(),
        )


@menu_router.callback_query(F.data.contains("flr"))
@menu_router.message(SalaryCountStates.FLR)
async def process_flr(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer(text=f"Процент премии за FLR - {query.data.split("_")[-1]}!")
    await state.update_data(FLR=query.data.split("_")[-1])
    await state.set_state(SalaryCountStates.GOK)

    user_data = await state.get_data()
    if user_data["POSITION"] == "specialist":
        await query.message.edit_text(
            "💯 Теперь введи процент премии за <b>ГОК</b>",
            reply_markup=salary_specialistist_gok(),
        )
    else:
        await query.message.edit_text(
            "💯 Теперь введи процент премии за <b>ГОК</b>",
            reply_markup=salary_supervisor_gok(),
        )


@menu_router.callback_query(F.data.contains("gok"))
@menu_router.message(SalaryCountStates.GOK)
async def process_gok(query: CallbackQuery, state: FSMContext) -> None:
    await query.answer(text=f"Процент премии за ГОК - {query.data.split("_")[-1]}!")
    await state.update_data(GOK=query.data.split("_")[-1])
    user_data = await state.get_data()
    if user_data["POSITION"] == "specialist":
        await state.set_state(SalaryCountStates.CLIENT_RATING)

        await query.message.edit_text(
            "📈 Теперь введи процент премии за <b>оценку от клиента</b>",
            reply_markup=salary_specialist_rate(),
        )
    else:
        await state.set_state(SalaryCountStates.CLIENT_RATING)

        await query.message.edit_text(
            "🏆 Теперь введи процент премии за <b>SL</b>",
            reply_markup=salary_supervisor_sl(),
        )


@menu_router.callback_query(F.data.contains("sl"))
@menu_router.message(SalaryCountStates.SL)
async def process_sl(query: CallbackQuery, state: FSMContext):
    await query.answer(text=f"Процент премии за SL - {query.data.split("_")[-1]}!")
    await state.update_data(SL=query.data.split("_")[-1])

    user_data = await state.get_data()
    salary = await salary_with_percents(
        position=user_data["POSITION"],
        hourly_payment=float(user_data["HOURLY_RATE"]),
        hours_worked=int(user_data["HOURS_WORKED"]),
        aht=int(user_data["AHT"]),
        flr=int(user_data["FLR"]),
        gok=int(user_data["GOK"]),
        sl=int(user_data["SL"]),
    )

    message = f"""
Спасибо! Вот введенные тобой показатели:
💼 <b>Должность</b>: Руководитель
🕖 <b>ЧТС</b>: {user_data["HOURLY_RATE"]} руб/час
⏳ <b>Отработано</b>: {user_data["HOURS_WORKED"]} часов
⚡ <b>AHT</b>: {user_data["AHT"]}%
⚙️ <b>FLR</b>: {user_data["FLR"]}%
💯 <b>ГОК</b>: {user_data["GOK"]}%
🏆 <b>SL</b>: {user_data["SL"]}%

Оклад составляет <b>{salary["hours_salary"]}</b> р.
Общий процент премии составляет <b>{salary["premium_percent"]}%</b>
Премия составляет <b>{salary["premium_salary"]}</b> р.
ЗП + Премия составляет <b>{salary["salary_sum"]}</b> р.
"""
    await query.message.edit_text(message)
    await state.clear()


@menu_router.callback_query(F.data.contains("rate"))
@menu_router.message(SalaryCountStates.CLIENT_RATING)
async def process_rate(query: CallbackQuery, state: FSMContext):
    await query.answer(text=f"Процент премии за ОК - {query.data.split("_")[-1]}!")
    await state.update_data(CLIENT_RATING=query.data.split("_")[-1])

    await state.set_state(SalaryCountStates.TESTS)

    await query.message.edit_text(
        "🧪 Теперь укажи сданы ли <b>все тесты</b>",
        reply_markup=salary_specialist_tests(),
    )


@menu_router.callback_query(F.data.contains("tests"))
@menu_router.message(SalaryCountStates.TESTS)
async def process_tests(query: CallbackQuery, state: FSMContext):
    await query.answer(text=f"Процент премии за ОК - {query.data.split("_")[-1]}!")
    await state.update_data(TESTS=query.data.split("_")[-1])
    # Получение данных пользователя

    user_data = await state.get_data()
    salary = await salary_with_percents(
        position=user_data["POSITION"],
        hourly_payment=float(user_data["HOURLY_RATE"]),
        hours_worked=int(user_data["HOURS_WORKED"]),
        aht=int(user_data["AHT"]),
        flr=int(user_data["FLR"]),
        gok=int(user_data["GOK"]),
        client_rating=int(user_data["CLIENT_RATING"]),
        tests=user_data["TESTS"],
    )

    message = f"""
Спасибо! Вот введенные тобой показатели:
💼 <b>Должность</b>: Специалист
🕖 <b>ЧТС</b>: {user_data["HOURLY_RATE"]} руб/час
⏳ <b>Отработано</b>: {user_data["HOURS_WORKED"]} часов
⚡ <b>AHT</b>: {user_data["AHT"]}%
⚙️ <b>FLR</b>: {user_data["FLR"]}%
💯 <b>ГОК</b>: {user_data["GOK"]}%
📈 <b>ОК</b>: {user_data["CLIENT_RATING"]}%
🧪 <b>Тесты</b>: {'5%' if("yes" in user_data["TESTS"]) else '0%'}

Оклад составляет <b>{salary["hours_salary"]}</b> р.
Общий процент премии составляет <b>{salary["premium_percent"]}%</b>
Премия составляет <b>{salary["premium_salary"]}</b> р.
ЗП + Премия составляет <b>{salary["salary_sum"]}</b> р.
"""
    await query.message.edit_text(message)
    await state.clear()


@menu_router.callback_query(F.data == "purchases_sales")
async def my_orders(query: CallbackQuery):
    await query.answer()
    await query.message.edit_text("Вы открыли ваши часики!")


# To filter the callback data, that was created with CallbackData factory, you can use .filter() method
@menu_router.callback_query(OrderCallbackData.filter())
async def show_order(query: CallbackQuery, callback_data: OrderCallbackData):
    await query.answer()

    # You can get the data from callback_data object as attributes
    order_id = callback_data.order_id

    # Then you can get the order from your database (here we use a simple list)
    order_info = next((order for order in ORDERS if order["id"] == order_id), None)

    if order_info:
        # Here we use aiogram.utils.formatting to format the text
        # https://docs.aiogram.dev/en/latest/utils/formatting.html
        text = as_section(
            as_key_value("Заказ #", order_info["id"]),
            as_marked_list(
                as_key_value("Товар", order_info["title"]),
                as_key_value("Статус", order_info["status"]),
            ),
        )

        await query.message.edit_text(text.as_html(), parse_mode=ParseMode.HTML)
    else:
        await query.message.edit_text("Часики не найдены!")

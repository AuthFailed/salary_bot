from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.formatting import as_section, as_key_value, as_marked_list
from aiogram.fsm.context import FSMContext

from tgbot.keyboards.inline import salary_menu, salary_menu_aht, \
    OrderCallbackData, salary_menu_flr, salary_menu_gok, salary_menu_client_rating
from tgbot.misc.states import SalaryCountStates

menu_router = Router()


@menu_router.message(Command("salary"))
async def show_menu(message: Message):
    await message.answer("Выберите пункт меню:", reply_markup=salary_menu())


# We can use F.data filter to filter callback queries by data field from CallbackQuery object
@menu_router.callback_query(F.data == "count_salary")
async def create_order(query: CallbackQuery, state: FSMContext):
    # Firstly, always answer callback query (as Telegram API requires)
    await query.answer()
    await state.set_state(SalaryCountStates.HOURLY_RATE)

    # This method will send an answer to the message with the button, that user pressed
    # Here query - is a CallbackQuery object, which contains message: Message object
    await query.message.edit_text("Давай посчитаем зарплату\nВведи часовую ставку в чат")


@menu_router.message(SalaryCountStates.HOURLY_RATE)
async def process_hourly_rate(message: Message, state: FSMContext) -> None:
    await state.update_data(HOURLY_RATE=message.text)
    await state.set_state(SalaryCountStates.HOURS_WORKED)
    await message.answer("⏳ Теперь введи <b>кол-во отработанных часов</b>")


@menu_router.message(SalaryCountStates.HOURS_WORKED)
async def process_hours_worked(message: Message, state: FSMContext) -> None:
    await state.update_data(HOURS_WORKED=message.text)
    await state.set_state(SalaryCountStates.AHT)

    await message.answer(
        "⚡ Введи процент премии за <b>AHT</b>",
        reply_markup=salary_menu_aht(),
    )


@menu_router.callback_query(F.data)
@menu_router.message(SalaryCountStates.AHT)
async def process_aht(query: CallbackQuery, state: FSMContext) -> None:
    await print(query)
    await state.update_data(AHT=query.data)
    await state.set_state(SalaryCountStates.FLR)

    await query.message.edit_text(
        "⚙️ Теперь выбери процент премии за <b>FLR</b>",
        reply_markup=salary_menu_flr(),
    )


@menu_router.message(SalaryCountStates.FLR)
async def process_flr(message: Message, state: FSMContext) -> None:
    await state.update_data(FLR=message.text)
    await state.set_state(SalaryCountStates.GOK)

    await message.answer(
        "💯 Теперь введи процент премии за <b>ГОК</b>",
        reply_markup=salary_menu_gok(),
    )


@menu_router.message(SalaryCountStates.GOK)
async def process_gok(message: Message, state: FSMContext) -> None:
    await state.update_data(GOK=message.text)
    await state.set_state(SalaryCountStates.CLIENT_RATING)

    await message.answer(
        "📈 Теперь введи процент премии за <b>оценку от клиента</b>",
        reply_markup=salary_menu_client_rating(),
    )


@menu_router.message(SalaryCountStates.CLIENT_RATING)
async def process_clien_rating(message: Message, state: FSMContext):
    await state.update_data(CLIENT_RATING=message.text)
    # Получение данных пользователя

    user_data = await state.get_data()
    salary = await utils.count_wage_with_percents(
        hourly_payment=float(user_data["HOURLY_RATE"].replace(",", ".").replace()),
        hours_worked=int(user_data["HOURS_WORKED"]),
        aht=int(user_data["AHT"]),
        flr=int(user_data["FLR"]),
        gok=int(user_data["GOK"]),
        client_rating=int(user_data["CLIENT_RATING"]),
    )

    await message.answer(
        f"""
Спасибо! Вот введенные тобой показатели:
🕖 <b>ЧТС</b>: {user_data["HOURLY_RATE"]}
⏳ <b>Отработано</b>: {user_data["HOURS_WORKED"]}
⚡ <b>AHT</b>: {user_data["AHT"]}%
⚙️ <b>FLR</b>: {user_data["FLR"]}%
💯 <b>ГОК</b>: {user_data["GOK"]}%
📈 <b>ОК</b>: {user_data["CLIENT_RATING"]}%

Оклад составляет <b>{salary["hours_salary"]}</b> р.
Общий процент премии составляет <b>{salary["premium_percent"]}%</b>
Премия составляет <b>{salary["premium_salary"]}</b> р.
ЗП + Премия составляет <b>{salary["salary_sum"]}</b> р.
"""
    )
    # Сброс состояний после получения данных
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

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


def salary_menu():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="💸 Расчет ЗП", callback_data="count_salary")
    keyboard.button(text="🏖️ Расчет отпускных", callback_data="count_vacation")
    return keyboard.as_markup()


def position():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="👨‍💻 Специалист", callback_data="position_specialist")
    keyboard.button(text="👮 Руководитель", callback_data="position_supervisor")

    return keyboard.as_markup()


def salary_coefficient():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="1", callback_data="coefficient_1")
    keyboard.button(text="1.15", callback_data="coefficient_1.15")
    keyboard.button(text="1.2", callback_data="coefficient_1.2")
    keyboard.button(text="1.25", callback_data="coefficient_1.25")
    keyboard.button(text="1.3", callback_data="coefficient_1.3")
    keyboard.button(text="1.4", callback_data="coefficient_1.4")
    keyboard.button(text="1.5", callback_data="coefficient_1.5")
    keyboard.button(text="1.6", callback_data="coefficient_1.6")
    keyboard.button(text="1.7", callback_data="coefficient_1.7")
    keyboard.button(text="1.8", callback_data="coefficient_1.8")
    keyboard.button(text="2", callback_data="coefficient_2")

    keyboard.adjust(3)
    return keyboard.as_markup()


def salary_specialistist_aht():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0%", callback_data="aht_0")
    keyboard.button(text="18%", callback_data="aht_18")
    keyboard.button(text="28%", callback_data="aht_28")

    return keyboard.as_markup()


def salary_supervisor_aht():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0%", callback_data="aht_0")
    keyboard.button(text="16%", callback_data="aht_16")
    keyboard.button(text="25%", callback_data="aht_25")

    return keyboard.as_markup()


def salary_specialistist_flr():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="8%", callback_data="flr_8")
    keyboard.button(text="13%", callback_data="flr_13")
    keyboard.button(text="18%", callback_data="flr_18")
    keyboard.button(text="21%", callback_data="flr_21")
    keyboard.button(text="25%", callback_data="flr_25")
    keyboard.button(text="30%", callback_data="flr_30")

    keyboard.adjust(3)
    return keyboard.as_markup()


def salary_supervisor_flr():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="10%", callback_data="flr_10")
    keyboard.button(text="14%", callback_data="flr_14")
    keyboard.button(text="16%", callback_data="flr_16")
    keyboard.button(text="18%", callback_data="flr_18")
    keyboard.button(text="23%", callback_data="flr_23")
    keyboard.button(text="25%", callback_data="flr_25")

    keyboard.adjust(3)
    return keyboard.as_markup()


def salary_specialistist_gok():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0%", callback_data="gok_0")
    keyboard.button(text="5%", callback_data="gok_5")
    keyboard.button(text="9%", callback_data="gok_9")
    keyboard.button(text="12%", callback_data="gok_12")
    keyboard.button(text="15%", callback_data="gok_15")
    keyboard.button(text="17%", callback_data="gok_17")

    keyboard.adjust(3)
    return keyboard.as_markup()


def salary_supervisor_gok():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0%", callback_data="gok_0")
    keyboard.button(text="10%", callback_data="gok_10")
    keyboard.button(text="12%", callback_data="gok_12")
    keyboard.button(text="14%", callback_data="gok_14")
    keyboard.button(text="16%", callback_data="gok_16")
    keyboard.button(text="18%", callback_data="gok_18")
    keyboard.button(text="20%", callback_data="gok_20")

    keyboard.adjust(3)
    return keyboard.as_markup()


def salary_specialist_rate():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0%", callback_data="rate_0")
    keyboard.button(text="5%", callback_data="rate_5")
    keyboard.button(text="10%", callback_data="rate_10")
    keyboard.button(text="15%", callback_data="rate_15")
    keyboard.button(text="20%", callback_data="rate_20")

    keyboard.adjust(3)
    return keyboard.as_markup()


def salary_specialist_tests():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Да", callback_data="tests_yes")
    keyboard.button(text="Нет", callback_data="tests_no")

    return keyboard.as_markup()


def salary_specialist_acknowledgments():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0%", callback_data="acknowledgments_0")
    keyboard.button(text="3%", callback_data="acknowledgments_3")
    keyboard.button(text="6%", callback_data="acknowledgments_6")

    return keyboard.as_markup()


def salary_specialist_mentor():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Да", callback_data="mentor_yes")
    keyboard.button(text="Нет", callback_data="mentor_no")

    return keyboard.as_markup()


def salary_specialist_mentor_type():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="3D", callback_data="typementor_3d")
    keyboard.button(text="Основной", callback_data="typementor_main")
    keyboard.button(text="Общий", callback_data="typementor_general")

    return keyboard.as_markup()


def salary_specialist_mentoring_days():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0", callback_data="daysmentoring_0")
    keyboard.button(text="1", callback_data="daysmentoring_1")
    keyboard.button(text="2", callback_data="daysmentoring_2")
    keyboard.button(text="3", callback_data="daysmentoring_3")
    keyboard.button(text="4", callback_data="daysmentoring_4")
    keyboard.button(text="5", callback_data="daysmentoring_5")
    keyboard.button(text="6", callback_data="daysmentoring_6")
    keyboard.button(text="7", callback_data="daysmentoring_7")
    keyboard.button(text="8", callback_data="daysmentoring_8")
    keyboard.button(text="9", callback_data="daysmentoring_9")
    keyboard.button(text="10", callback_data="daysmentoring_10")
    keyboard.button(text="11", callback_data="daysmentoring_11")
    keyboard.button(text="12", callback_data="daysmentoring_12")
    keyboard.button(text="13", callback_data="daysmentoring_13")
    keyboard.button(text="14", callback_data="daysmentoring_14")
    keyboard.button(text="15", callback_data="daysmentoring_15")
    keyboard.button(text="16", callback_data="daysmentoring_16")

    keyboard.adjust(4)
    return keyboard.as_markup()


def salary_supervisor_sl():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0", callback_data="sl_0")
    keyboard.button(text="5", callback_data="sl_5")
    keyboard.button(text="10", callback_data="sl_10")

    return keyboard.as_markup()


def share(content: str = ""):
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="Поделиться", switch_inline_query={content})

    return keyboard.as_markup()


def admin_main_menu():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="💸 Расчет ЗП", callback_data="count_salary")
    keyboard.button(text="🏖️ Расчет отпускных", callback_data="count_vacation")
    keyboard.button(text="⚙️ Настройки", callback_data="admin_settings")
    keyboard.button(text="👥 Пользователи", callback_data="admin_users")
    keyboard.button(text="📢 Рассылка", callback_data="admin_broadcast")

    keyboard.adjust(2)
    return keyboard.as_markup()


# For a more advanced usage of callback_data, you can use the CallbackData factory
class OrderCallbackData(CallbackData, prefix="hours"):
    """
    This class represents a CallbackData object for orders.
    - When used in InlineKeyboardMarkup, you have to create an instance of this class, run .pack() method, and pass to callback_data parameter.
    - When used in InlineKeyboardBuilder, you have to create an instance of this class and pass to callback_data parameter (without .pack() method).
    - In handlers you have to import this class and use it as a filter for callback query handlers, and then unpack callback_data parameter to get the data.
    # Example usage in simple_menu.py
    """

    order_id: int


def my_hours_keyboard(orders: list):
    # Here we use a list of orders as a parameter (from simple_menu.py)

    keyboard = InlineKeyboardBuilder()
    for order in orders:
        keyboard.button(
            text=f"📝 {order['title']}",
            # Here we use an instance of OrderCallbackData class as callback_data parameter
            # order id is the field in OrderCallbackData class, that we defined above
            callback_data=OrderCallbackData(order_id=order["id"]),
        )

    return keyboard.as_markup()

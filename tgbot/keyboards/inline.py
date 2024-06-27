from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


def salary_menu():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="💸 Посчитать кокосики", callback_data="count_salary")
    keyboard.button(text="💎 Покупки/продажи", callback_data="purchases_sales")

    return keyboard.as_markup()


def salary_menu_aht():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0%", callback_data="aht_0")
    keyboard.button(text="18%", callback_data="aht_18")
    keyboard.button(text="28%", callback_data="aht_28")

    return keyboard.as_markup()


def salary_menu_flr():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="8%", callback_data="flr_8")
    keyboard.button(text="13%", callback_data="flr_13")
    keyboard.button(text="18%", callback_data="flr_18")
    keyboard.button(text="21%", callback_data="flr_21")
    keyboard.button(text="25%", callback_data="flr_25")
    keyboard.button(text="30%", callback_data="flr_30")

    keyboard.adjust(3)
    return keyboard.as_markup()


def salary_menu_gok():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0%", callback_data="gok_0")
    keyboard.button(text="5%", callback_data="gok_5")
    keyboard.button(text="9%", callback_data="gok_9")
    keyboard.button(text="12%", callback_data="gok_12")
    keyboard.button(text="15%", callback_data="gok_15")
    keyboard.button(text="17%", callback_data="gok_17")

    keyboard.adjust(3)
    return keyboard.as_markup()


def salary_menu_client_rating():
    keyboard = InlineKeyboardBuilder()

    keyboard.button(text="0%", callback_data="rate_0")
    keyboard.button(text="5%", callback_data="rate_5")
    keyboard.button(text="10%", callback_data="rate_10")
    keyboard.button(text="15%", callback_data="rate_15")
    keyboard.button(text="20%", callback_data="rate_20")

    keyboard.adjust(3)
    return keyboard.as_markup()


# For a more advanced usage of callback_data, you can use the CallbackData factory
class OrderCallbackData(CallbackData, prefix="order"):
    """
    This class represents a CallbackData object for orders.

    - When used in InlineKeyboardMarkup, you have to create an instance of this class, run .pack() method, and pass to callback_data parameter.

    - When used in InlineKeyboardBuilder, you have to create an instance of this class and pass to callback_data parameter (without .pack() method).

    - In handlers you have to import this class and use it as a filter for callback query handlers, and then unpack callback_data parameter to get the data.

    # Example usage in simple_menu.py
    """

    order_id: int


def my_orders_keyboard(orders: list):
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

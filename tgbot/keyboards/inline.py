from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


# This is the same keyboard, but created with InlineKeyboardBuilder (preferred way)
def salary_menu():
    # First, you should create an InlineKeyboardBuilder object
    keyboard = InlineKeyboardBuilder()

    # You can use keyboard.button() method to add buttons, then enter text and callback_data
    keyboard.button(
        text="💸 Посчитать кокосики",
        callback_data="count_salary"
    )
    keyboard.button(
        text="💎 Покупки/продажи",
        callback_data="purchases_sales"
    )

    # If needed you can use keyboard.adjust() method to change the number of buttons per row
    # keyboard.adjust(2)

    # Then you should always call keyboard.as_markup() method to get a valid InlineKeyboardMarkup object
    return keyboard.as_markup()


def salary_menu_aht():
    # First, you should create an InlineKeyboardBuilder object
    keyboard = InlineKeyboardBuilder()

    # You can use keyboard.button() method to add buttons, then enter text and callback_data
    keyboard.button(
        text="0%",
        callback_data="aht_0"
    )
    keyboard.button(
        text="18%",
        callback_data="aht_18"
    )
    keyboard.button(
        text="28%",
        callback_data="aht_28"
    )

    # If needed you can use keyboard.adjust() method to change the number of buttons per row
    # keyboard.adjust(2)

    # Then you should always call keyboard.as_markup() method to get a valid InlineKeyboardMarkup object
    return keyboard.as_markup()


def salary_menu_flr():
    # First, you should create an InlineKeyboardBuilder object
    keyboard = InlineKeyboardBuilder()

    # You can use keyboard.button() method to add buttons, then enter text and callback_data
    keyboard.button(
        text="8%",
        callback_data="flr_0"
    )
    keyboard.button(
        text="13%",
        callback_data="flr_18"
    )
    keyboard.button(
        text="18%",
        callback_data="flr_18"
    )
    keyboard.button(
        text="21%",
        callback_data="flr_21"
    )
    keyboard.button(
        text="25%",
        callback_data="flr_25"
    )
    keyboard.button(
        text="30%",
        callback_data="flr_30"
    )

    # If needed you can use keyboard.adjust() method to change the number of buttons per row
    # keyboard.adjust(2)

    # Then you should always call keyboard.as_markup() method to get a valid InlineKeyboardMarkup object
    return keyboard.as_markup()


def salary_menu_gok():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(
        text="0%",
        callback_data="gok_0"
    )
    keyboard.button(
        text="0%",
        callback_data="gok_18"
    )
    keyboard.button(
        text="9%",
        callback_data="gok_28"
    )
    keyboard.button(
        text="12%",
        callback_data="gok_28"
    )
    keyboard.button(
        text="15%",
        callback_data="gok_28"
    )
    keyboard.button(
        text="17%",
        callback_data="gok_28"
    )

    # If needed you can use keyboard.adjust() method to change the number of buttons per row
    # keyboard.adjust(2)

    # Then you should always call keyboard.as_markup() method to get a valid InlineKeyboardMarkup object
    return keyboard.as_markup()


def salary_menu_client_rating():
    keyboard = InlineKeyboardBuilder()
    
    keyboard.button(
        text="0%",
        callback_data="rate_0"
    )
    keyboard.button(
        text="5%",
        callback_data="rate_5"
    )
    keyboard.button(
        text="10%",
        callback_data="rate_10"
    )
    keyboard.button(
        text="15%",
        callback_data="rate_15"
    )
    keyboard.button(
        text="20%",
        callback_data="rate_20"
    )

    # If needed you can use keyboard.adjust() method to change the number of buttons per row
    # keyboard.adjust(2)

    # Then you should always call keyboard.as_markup() method to get a valid InlineKeyboardMarkup object
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
            callback_data=OrderCallbackData(order_id=order["id"])
        )

    return keyboard.as_markup()

from tgbot.keyboards.inline import admin_main_menu

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from tgbot.filters.admin import AdminFilter

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.reply(
        f"Привет, @{message.from_user.username}!\nИспользуй меню для управления ботом",
        reply_markup=admin_main_menu(),
    )

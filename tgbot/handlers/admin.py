from tgbot.keyboards.inline import admin_main_menu
from aiogram import F
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import CallbackQuery


from tgbot.filters.admin import AdminFilter
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
    salary_coefficient,
    salary_specialist_acknowledgments,
    salary_specialist_mentor,
    salary_specialist_mentoring_days,
    salary_specialist_mentor_type,
    count_type,
)

admin_router = Router()
admin_router.message.filter(AdminFilter())


@admin_router.message(CommandStart())
async def admin_start(message: Message):
    await message.reply(
        f"Привет, @{message.from_user.username}!\nИспользуй меню для управления ботом",
        reply_markup=admin_main_menu(),
    )

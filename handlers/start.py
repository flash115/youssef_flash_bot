from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.menu import main_menu

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "👋 أهلاً بك في Youssef Flash Bot\n\n"
        "📧 اضغط على الأزرار بالأسفل للبدء.",
        reply_markup=main_menu
    )

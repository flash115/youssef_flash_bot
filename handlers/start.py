from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    await message.answer(
        "📧 أهلاً بك في بوت البريد المؤقت.\n\n"
        "اضغط على الأزرار لبدء الاستخدام."
    )

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="📧 إنشاء بريد", callback_data="new_mail")],
        [InlineKeyboardButton(text="📥 صندوق الوارد", callback_data="inbox")],
        [InlineKeyboardButton(text="🔄 تحديث", callback_data="refresh")],
        [InlineKeyboardButton(text="🗑 حذف البريد", callback_data="delete_mail")]
    ]
)

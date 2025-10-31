from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Основная клавиатура с кнопками для броска кубиков"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🎲 1d4"), KeyboardButton(text="🎲 1d6")],
            [KeyboardButton(text="🎲 1d8"), KeyboardButton(text="🎲 1d10")],
            [KeyboardButton(text="🎲 1d12"), KeyboardButton(text="🎲 1d20")],
            [KeyboardButton(text="🎲 2d6"), KeyboardButton(text="🎲 3d6")],
            [KeyboardButton(text="🎲 Произвольный кубик"), KeyboardButton(text="ℹ️ Помощь")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите кубик для броска..."
    )
    return keyboard

def get_custom_dice_keyboard() -> InlineKeyboardMarkup:
    """Инлайн клавиатура для произвольных кубиков"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1d4", callback_data="custom_1d4"),
             InlineKeyboardButton(text="1d6", callback_data="custom_1d6"),
             InlineKeyboardButton(text="1d8", callback_data="custom_1d8")],
            [InlineKeyboardButton(text="1d10", callback_data="custom_1d10"),
             InlineKeyboardButton(text="1d12", callback_data="custom_1d12"),
             InlineKeyboardButton(text="1d20", callback_data="custom_1d20")],
            [InlineKeyboardButton(text="2d6", callback_data="custom_2d6"),
             InlineKeyboardButton(text="3d6", callback_data="custom_3d6"),
             InlineKeyboardButton(text="2d20", callback_data="custom_2d20")],
        ]
    )
    return keyboard
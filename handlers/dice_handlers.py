from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from utils.dice_roller import DiceRoller
from keyboards.dice_keyboards import get_main_keyboard, get_custom_dice_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    """Обработчик команды /start"""
    welcome_text = """
    🐉 Добро пожаловать в D&D Dice Bot! 🎲

    Я помогу вам бросать кубики для настольных ролевых игр.

    Доступные команды:
    /start - начать работу
    /help - показать справку
    /custom - бросить произвольный кубик

    Просто нажмите на кнопку ниже чтобы бросить кубик!
    """
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

@router.message(Command("help"))
async def cmd_help(message: Message):
    """Обработчик команды /help"""
    help_text = """
    🎲 **Как пользоваться ботом:**

    • Используйте кнопки для быстрого броска стандартных кубиков
    • Формат кубиков: XdY, где:
      X - количество кубиков
      Y - количество граней

    📊 **Примеры:**
    1d4 - один 4-гранный кубик
    2d6 - два 6-гранных кубика
    3d20 - три 20-гранных кубика

    ⚡ **Быстрые команды:**
    /custom - бросить произвольный кубик
    """
    await message.answer(help_text, reply_markup=get_main_keyboard())

@router.message(Command("custom"))
async def cmd_custom(message: Message):
    """Обработчик команды для произвольного броска"""
    await message.answer(
        "Выберите кубик для броска:",
        reply_markup=get_custom_dice_keyboard()
    )

# Обработчики для кнопок основных кубиков
@router.message(F.text.startswith("🎲"))
async def handle_dice_buttons(message: Message):
    """Обработчик нажатий на кнопки кубиков"""
    try:
        # Извлекаем тип кубика из текста кнопки
        dice_type = message.text.replace("🎲", "").strip()
        
        if dice_type == "Произвольный кубик":
            await cmd_custom(message)
            return
        
        result = DiceRoller.roll_dice(dice_type)
        response = DiceRoller.format_result(result)
        await message.answer(response, reply_markup=get_main_keyboard())
        
    except ValueError as e:
        await message.answer(f"❌ Ошибка: {e}", reply_markup=get_main_keyboard())

# Обработчик инлайн кнопок для произвольных кубиков
@router.callback_query(F.data.startswith("custom_"))
async def handle_custom_dice(callback: CallbackQuery):
    """Обработчик инлайн кнопок произвольных кубиков"""
    try:
        # Извлекаем тип кубика из callback_data
        dice_type = callback.data.replace("custom_", "")
        
        result = DiceRoller.roll_dice(dice_type)
        response = DiceRoller.format_result(result)
        
        await callback.message.edit_text(
            f"{response}\n\n🎯 Нажмите /custom для нового броска"
        )
        await callback.answer()
        
    except ValueError as e:
        await callback.message.edit_text(f"❌ Ошибка: {e}")
        await callback.answer()

@router.message(F.text == "ℹ️ Помощь")
async def handle_help_button(message: Message):
    """Обработчик кнопки помощи"""
    await cmd_help(message)

# Обработчик текстовых команд с произвольными кубиками
@router.message(F.text.regexp(r'^\d*d?\d+$'))
async def handle_text_dice(message: Message):
    """Обработчик текстового ввода кубиков (например: 2d6, 1d20, d6)"""
    try:
        dice_type = message.text.lower()
        if dice_type.startswith('d'):
            dice_type = '1' + dice_type
            
        result = DiceRoller.roll_dice(dice_type)
        response = DiceRoller.format_result(result)
        await message.answer(response, reply_markup=get_main_keyboard())
        
    except ValueError as e:
        await message.answer(
            f"❌ Некорректный формат кубика. Используйте формат: XdY\n"
            f"Примеры: 1d20, 2d6, d8 (эквивалентно 1d8)",
            reply_markup=get_main_keyboard()
        )
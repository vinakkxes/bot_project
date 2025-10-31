import random

class DiceRoller:
    @staticmethod
    def roll_dice(dice_type: str) -> dict:
        """
        Бросает кубик указанного типа
        Возвращает словарь с результатом
        """
        try:
            # Извлекаем количество кубиков и граней
            if 'd' in dice_type:
                parts = dice_type.lower().split('d')
                num_dice = int(parts[0]) if parts[0] else 1
                sides = int(parts[1])
            else:
                num_dice = 1
                sides = int(dice_type)
            
            if num_dice <= 0 or sides <= 0:
                raise ValueError("Некорректные параметры кубика")
            
            # Бросаем кубики
            rolls = [random.randint(1, sides) for _ in range(num_dice)]
            total = sum(rolls)
            
            return {
                'dice_type': dice_type,
                'num_dice': num_dice,
                'sides': sides,
                'rolls': rolls,
                'total': total,
                'formula': f"{num_dice}d{sides}"
            }
            
        except (ValueError, IndexError):
            raise ValueError(f"Некорректный формат кубика: {dice_type}")
    
    @staticmethod
    def format_result(result: dict) -> str:
        """Форматирует результат броска для вывода"""
        if result['num_dice'] == 1:
            return f"🎲 {result['formula']}: {result['total']}"
        else:
            rolls_str = ' + '.join(map(str, result['rolls']))
            return f"🎲 {result['formula']}: {rolls_str} = {result['total']}"
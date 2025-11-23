from typing import Tuple

def get_difficulty_preset(level: str) -> Tuple[int, bool]:
    presets = {
        "легкий": (None, True),    # нет лимита, с подсказками
        "средний": (30, False),  # 30 секунд, без подсказок
        "сложный": (15, False)   # 15 секунд, без подсказок
    }
    return presets.get(level, (30, False))  # значения по умолчанию

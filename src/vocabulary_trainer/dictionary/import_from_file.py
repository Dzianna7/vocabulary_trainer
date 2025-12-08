import os
import json
from src.vocabulary_trainer.core.models import Vocabulary


def import_from_file(vocabulary: Vocabulary, filepath: str) -> int:
    """
    Импортирует слова из файла

    Args:
        vocabulary: Словарь
        filepath: Путь к файлу

    Returns:
        int: Количество импортированных слов

    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: Если формат файла не поддерживается
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Файл {filepath} не найден")

    file_ext = os.path.splitext(filepath)[1].lower()
    imported_count = 0

    if file_ext == '.json':
        imported_count = _import_from_json(vocabulary, filepath)
    elif file_ext in ['.txt', '.csv']:
        imported_count = _import_from_text(vocabulary, filepath)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {file_ext}")

    return imported_count


def _import_from_json(vocabulary: Vocabulary, filepath: str) -> int:
    """Импорт из JSON файла"""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    imported_count = 0
    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and 'word' in item and 'translation' in item:
                if vocabulary.add_word(item['word'], item['translation']):
                    imported_count += 1
    elif isinstance(data, dict):
        for word, translation in data.items():
            if vocabulary.add_word(word, translation):
                imported_count += 1

    return imported_count


def _import_from_text(vocabulary: Vocabulary, filepath: str) -> int:
    """Импорт из текстового файла"""
    imported_count = 0

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            # Поддержка форматов: слово - перевод, слово, перевод, слово: перевод
            separators = [' - ', ',', ':', ';', '\t']
            for sep in separators:
                if sep in line:
                    parts = line.split(sep, 1)
                    if len(parts) == 2:
                        word, translation = parts[0].strip(), parts[1].strip()
                        if word and translation:
                            if vocabulary.add_word(word, translation):
                                imported_count += 1
                        break

    return imported_count
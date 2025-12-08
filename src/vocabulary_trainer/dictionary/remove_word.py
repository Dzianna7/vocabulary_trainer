from src.vocabulary_trainer.core.models import Vocabulary
from src.vocabulary_trainer.core.exceptions import WordNotFoundError


def remove_word(vocabulary: Vocabulary, word: str) -> bool:
    """
    Удаляет слово из словаря

    Args:
        vocabulary: Словарь, содержащий в себе пул слов с переводом
        word: Слово для удаления

    Returns:
        bool: True если слово удалено

    Raises:
        WordNotFoundError: Если слово не найдено в словаре
    """
    if vocabulary.remove_word(word.strip()):
        return True
    else:
        raise WordNotFoundError(f"Слово '{word}' не найдено в словаре")
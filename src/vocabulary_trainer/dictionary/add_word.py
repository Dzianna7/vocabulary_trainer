from src.vocabulary_trainer.core.models import Vocabulary
from src.vocabulary_trainer.core.exceptions import WordAlreadyExistsError


def add_word(vocabulary: Vocabulary, word: str, translation: str) -> bool:
    """
    Добавляет слово в словарь

    Args:
        vocabulary: Словарь, содержащий в себе пул слов с переводом
        word: Слово на иностранном языке
        translation: Перевод слова

    Returns:
        bool: True если слово добавлено

    Raises:
        ValueError: Если слово или перевод пустые
        WordAlreadyExistsError: Если слово уже существует в словаре
    """
    word = word.strip()
    translation = translation.strip()

    # check if the input is not empty
    if not word or not translation:
        raise ValueError("Слово и перевод не могут быть пустыми")

    # adding a word
    if not vocabulary.add_word(word, translation):
        raise WordAlreadyExistsError(f"Слово '{word}' уже существует в словаре")

    return True
from src.vocabulary_trainer.core.models import Vocabulary
from src.vocabulary_trainer.core.exceptions import EmptyVocabularyError


def show_all_words(vocabulary: Vocabulary) -> list:
    """
    Показывает все слова в словаре

    Args:
        vocabulary: Словарь

    Returns:
        list: Список слов

    Raises:
        EmptyVocabularyError: Если словарь пуст
    """
    words = vocabulary.get_all_words()
    if not words:
        raise EmptyVocabularyError("Словарь пуст")

    return words
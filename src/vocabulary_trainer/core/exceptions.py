class VocabularyError(Exception):
    """Базовое исключение для словаря"""
    pass

class WordAlreadyExistsError(VocabularyError):
    """Слово уже существует в словаре"""
    pass

class WordNotFoundError(VocabularyError):
    """Слово не найдено в словаре"""
    pass

class EmptyVocabularyError(VocabularyError):
    """Словарь пуст"""
    pass

class QuizError(Exception):
    """Базовое исключение для квиза"""
    pass

class NotEnoughWordsError(QuizError):
    """Недостаточно слов для квиза"""
    pass
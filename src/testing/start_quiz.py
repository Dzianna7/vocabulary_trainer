from typing import Dict
from src.classes import QuizSession


def start_quiz(words_count: int, mode: str, vocabulary: Dict[str, str]) -> 'QuizSession':
    """
    Initialize and start a new quiz session.

    Args:
        words_count (int): Number of words to include in the quiz
        mode (str): Quiz mode - 'en_to_ru', 'ru_to_en', or 'mixed'
        vocabulary (Dict[str, str]): Dictionary of words and translations

    Returns:
        QuizSession: Initialized quiz session object

    Example:
        >>> vocab = {"apple": "яблоко", "book": "книга"}
        >>> session = start_quiz(2, "en_to_ru", vocab)
        >>> session.words_count
        2
    """
    pass
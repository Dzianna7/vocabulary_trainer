def ask_question(word: str, translation: str, mode: str) -> bool:
    """
    Ask a single question and validate the user's answer.

    Args:
        word (str): The word in original language
        translation (str): The translation of the word
        mode (str): Direction of translation - 'en_to_ru' or 'ru_to_en'

    Returns:
        bool: True if answer is correct, False otherwise

    Example:
        >>> ask_question("apple", "яблоко", "en_to_ru")
        Переведите 'apple': яблоко
        True
        >>> ask_question("apple", "яблоко", "en_to_ru")
        Переведите 'apple': дом
        False
    """
    pass

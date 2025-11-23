def add_word(word: str, translation: str) -> bool:
    """
    Add a new word and its translation to the vocabulary.

    Args:
        word (str): The word to add (e.g., "apple")
        translation (str): The translation of the word (e.g., "яблоко")

    Returns:
        bool: True if word was successfully added, False if word already exists

    Example:
        >>> add_word("book", "книга")
        True
        >>> add_word("book", "книга")
        False  # word already exists
    """
    pass
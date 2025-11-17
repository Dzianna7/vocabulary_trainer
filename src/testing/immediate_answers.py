def mark_correct(word: str) -> None:
    """
    Mark a word as correctly answered and update its statistics.

    Args:
        word (str): The word that was correctly answered

    Returns:
        None: Updates the word's statistics in place

    Example:
        >>> mark_correct("apple")
        # Updates correct_answers count and last_tested timestamp for "apple"
    """
    pass


def mark_incorrect(word: str) -> None:
    """
    Mark a word as incorrectly answered and update its statistics.

    Args:
        word (str): The word that was incorrectly answered

    Returns:
        None: Updates the word's statistics in place

    Example:
        >>> mark_incorrect("book")
        # Updates incorrect_answers count and last_tested timestamp for "book"
    """
    pass
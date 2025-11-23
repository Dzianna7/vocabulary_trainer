from typing import List, Dict


def calculate_score(results: List[bool]) -> Dict:
    """
    Calculate and return quiz results statistics.

    Args:
        results (List[bool]): List of boolean values representing correct/incorrect answers

    Returns:
        Dict: Dictionary containing score statistics

    Example:
        >>> calculate_score([True, False, True, True])
        {
            'total': 4,
            'correct': 3,
            'incorrect': 1,
            'score_percent': 75.0,
            'score_letter': 'C'
        }
    """
    pass
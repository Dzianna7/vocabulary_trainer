from typing import Dict
from src.vocabulary_trainer.core.models import QuizSession


def calculate_score(quiz_session: QuizSession) -> Dict:
    """
    Рассчитывает результаты квиза

    Args:
        quiz_session: Завершенная сессия квиза

    Returns:
        Dict: Статистика результатов
    """
    if not quiz_session.answers:
        return {
            'total_questions': 0,
            'correct_answers': 0,
            'incorrect_answers': 0,
            'success_rate': 0.0
        }

    correct_answers = sum(1 for answer in quiz_session.answers if answer['is_correct'])
    total_questions = len(quiz_session.answers)

    return {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': total_questions - correct_answers,
        'success_rate': (correct_answers / total_questions) * 100
    }
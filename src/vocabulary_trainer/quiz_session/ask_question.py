# Нет докстрингов, импорты не отсортированы

from typing import Optional, Dict, Any, Union  # Такая типизация устарела.
# `Any` желательно не использовать. В вашем коде вы могли точно указать тип.
from src.vocabulary_trainer.core.models import QuizSession  # Неправильный импорт.

def get_current_question(quiz_session: QuizSession) -> Optional[Dict[str, Any]]:
    if quiz_session.is_completed():
        return None

    return quiz_session.questions[quiz_session.current_question_index]


def get_question_text(question_data: Dict[str, Any]) -> str:
    return f"Translate the word: '{question_data['question']}'"


def submit_answer(quiz_session: QuizSession, user_answer: str) -> bool:
    if quiz_session.is_completed():
        return False

    current_question = quiz_session.questions[quiz_session.current_question_index]
    is_correct = (
        user_answer.strip().lower() == current_question["correct_answer"].lower()
    )

    quiz_session.answers.append(
        {
            "question": current_question["question"],
            "correct_answer": current_question["correct_answer"],
            "user_answer": user_answer,
            "is_correct": is_correct,
            "type": current_question["type"],
        }
    )

    quiz_session.current_question_index += 1
    return is_correct

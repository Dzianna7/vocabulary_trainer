# Не везде есть докстринги, импорты не отсортированы

import random
from src.vocabulary_trainer.core.models import Vocabulary  # Неправильные импорты. Все из-за того, что вы не заполнили `__init__.py`
from src.vocabulary_trainer.core.models import QuizSession
from src.vocabulary_trainer.core.exceptions import NotEnoughWordsError


def create_quiz(vocabulary: Vocabulary, words_count: int, mode: str) -> QuizSession:
    """
    Creates a new quiz session with questions.

    Args:
        vocabulary: Dictionary containing words.
        words_count: Number of words to include in the quiz.
        mode: Quiz mode - 'word_to_translation', 'translation_to_word', or 'mixed'.
    """
    available_words = vocabulary.get_words_count()
    if available_words < words_count:
        raise NotEnoughWordsError(
            f"Not enough words in dictionary. Available: {available_words}, required: {words_count}"
        )

    valid_modes = {"word_to_translation", "translation_to_word", "mixed"}
    if mode not in valid_modes:
        raise ValueError(
            f"Invalid mode. Valid values: {', '.join(sorted(valid_modes))}"
        )

    quiz = QuizSession(words_count=words_count, mode=mode, vocabulary=vocabulary)

    quiz_words = vocabulary.get_words_for_quiz(words_count)

    for word_obj in quiz_words:
        if mode == "mixed":
            question_type = random.choice(
                ["word_to_translation", "translation_to_word"]
            )
        else:
            question_type = mode

        if question_type == "word_to_translation":
            question_text = word_obj.word
            correct_answer = word_obj.translation
        else:
            question_text = word_obj.translation
            correct_answer = word_obj.word

        quiz.questions.append(
            {
                "type": question_type,
                "question": question_text,
                "correct_answer": correct_answer,
                "word_object": word_obj,
            }
        )

    return quiz


def update_word_statistics(quiz: QuizSession) -> None:
    if not quiz.answers:
        return

    # Слишком много "ступенек". Можно было написать проще
    for i, answer in enumerate(quiz.answers):
        if i < len(quiz.questions):
            question = quiz.questions[i]
            word_obj = question.get("word_object")
            if word_obj:
                if answer.get("is_correct", False):
                    word_obj.correct_answers += 1
                else:
                    word_obj.incorrect_answers += 1

import random
from src.vocabulary_trainer.core.models import QuizSession, Vocabulary
from src.vocabulary_trainer.core.exceptions import NotEnoughWordsError


def start_quiz(vocabulary: Vocabulary, words_count, mode) -> QuizSession:
    """
    Запускает новую сессию квиза

    Args:
        vocabulary: Словарь
        words_count: Количество слов для тестирования
        mode: Режим тестирования ('word_to_translation', 'translation_to_word', 'mixed')

    Returns:
        QuizSession: Сессия квиза

    Raises:
        NotEnoughWordsError: Если в словаре недостаточно слов
        ValueError: Если указан неверный режим
    """
    if vocabulary.get_words_count() < words_count:
        raise NotEnoughWordsError(
            f"Недостаточно слов в словаре. Доступно: {vocabulary.get_words_count()}, требуется: {words_count}"
        )

    valid_modes = ['word_to_translation', 'translation_to_word', 'mixed']
    if mode not in valid_modes:
        raise ValueError(f"Неверный режим. Допустимые значения: {', '.join(valid_modes)}")

    quiz_session = QuizSession(words_count, mode, vocabulary)

    # choosing words for the quiz
    quiz_words = vocabulary.get_words_for_quiz(words_count)

    # different modes of questions
    for word_obj in quiz_words:
        if mode == 'word_to_translation':
            quiz_session.questions.append({
                'type': 'word_to_translation',
                'question': word_obj.word,
                'correct_answer': word_obj.translation,
                'word_object': word_obj
            })
        elif mode == 'translation_to_word':
            quiz_session.questions.append({
                'type': 'translation_to_word',
                'question': word_obj.translation,
                'correct_answer': word_obj.word,
                'word_object': word_obj
            })
        else:  # mixed
            if random.choice([True, False]):
                quiz_session.questions.append({
                    'type': 'word_to_translation',
                    'question': word_obj.word,
                    'correct_answer': word_obj.translation,
                    'word_object': word_obj
                })
            else:
                quiz_session.questions.append({
                    'type': 'translation_to_word',
                    'question': word_obj.translation,
                    'correct_answer': word_obj.word,
                    'word_object': word_obj
                })

    return quiz_session
from src.vocabulary_trainer.quiz_session.test_difficulty import get_time_limit, get_first_letter_hint
from src.vocabulary_trainer.quiz_session.test_difficulty import format_time

import random
import time
from src.vocabulary_trainer.core.models import QuizSession
from src.vocabulary_trainer.core.exceptions import NotEnoughWordsError
from src.vocabulary_trainer.quiz_session.ask_question import get_current_question, get_question_text, submit_answer


def create_quiz(vocabulary, words_count: int, mode: str):
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

    valid_modes = {'word_to_translation', 'translation_to_word', 'mixed'}
    if mode not in valid_modes:
        raise ValueError(f"Invalid mode. Valid values: {', '.join(sorted(valid_modes))}")

    quiz = QuizSession(words_count=words_count, mode=mode, vocabulary=vocabulary)

    quiz_words = vocabulary.get_words_for_quiz(words_count)

    for word_obj in quiz_words:
        if mode == 'mixed':
            question_type = random.choice(['word_to_translation', 'translation_to_word'])
        else:
            question_type = mode

        if question_type == 'word_to_translation':
            question_text = word_obj.word
            correct_answer = word_obj.translation
        else:
            question_text = word_obj.translation
            correct_answer = word_obj.word

        quiz.questions.append({
            'type': question_type,
            'question': question_text,
            'correct_answer': correct_answer,
            'word_object': word_obj
        })

    return quiz

def conduct_quiz(quiz, level):
    """
    Conducts the quiz with difficulty-specific features.

    Args:
        quiz: Quiz session to conduct.
        level: Difficulty level (1-easy, 2-medium, 3-hard).
    """
    time_limit = get_time_limit(level, quiz.words_count)

    print(f"\n{'=' * 40}")
    print("QUIZ STARTED")
    print(f"{'=' * 40}")
    print(f"Difficulty: {'Easy' if level == 1 else 'Medium' if level == 2 else 'Hard'}")
    print(f"Mode: {quiz.mode.title().replace('_', ' ')}")
    print(f"Questions: {quiz.words_count}")

    if time_limit > 0:
        print(f"Time limit: {format_time(time_limit)}")
    else:
        print("Time limit: Unlimited")

    print(f"{'=' * 40}")

    start_time = time.time()

    question_number = 1
    correct_answers = 0

    while not quiz.is_completed():
        if time_limit > 0:
            elapsed = time.time() - start_time
            remaining = max(0, time_limit - int(elapsed))

            if remaining <= 0:
                print(f"\n⏰ TIME'S UP!")
                break

            print(f"\n⏱️  Time remaining: {format_time(remaining)}")

        current_question = get_current_question(quiz)
        if not current_question:
            break

        question_text = get_question_text(current_question)
        word_obj = current_question.get('word_object')

        print(f"\nQuestion {question_number}/{quiz.words_count}:")

        if level == 1 and word_obj:
            want_hint = input(f"{question_text} (need hint? y/n): ").strip().lower()

            if want_hint == 'y':
                hint = get_first_letter_hint(word_obj, current_question['type'])
                print(f"   💡 {hint}")

        if time_limit > 0:
            elapsed = time.time() - start_time
            remaining = max(0, time_limit - int(elapsed))

            if remaining <= 0:
                user_answer = ""
                print("⏰ Time's up!")
            else:
                print(f"[{format_time(remaining)} remaining]")
                user_answer = input(f"{question_text}: ").strip()
        else:
            user_answer = input(f"{question_text}: ").strip()

        is_correct = submit_answer(quiz, user_answer)

        if is_correct:
            print("✅ Correct!")
            correct_answers += 1
        else:
            print(f"❌ Incorrect. The correct answer is: {current_question['correct_answer']}")

        question_number += 1

    total_questions = min(quiz.words_count, question_number - 1)
    if total_questions > 0:
        success_rate = (correct_answers / total_questions) * 100
    else:
        success_rate = 0

    results = {
        'total_questions': total_questions,
        'correct_answers': correct_answers,
        'incorrect_answers': total_questions - correct_answers,
        'success_rate': success_rate,
        'time_limit_exceeded': time_limit > 0 and (time.time() - start_time) >= time_limit
    }

    return results


def display_results(results, level):
    print(f"\n{'=' * 40}")
    print("QUIZ RESULTS")
    print(f"{'=' * 40}")
    print(f"Difficulty: {'Easy' if level == 1 else 'Medium' if level == 2 else 'Hard'}")
    print(f"Total Questions: {results['total_questions']}")
    print(f"Correct Answers: {results['correct_answers']}")
    print(f"Incorrect Answers: {results['incorrect_answers']}")
    print(f"Success Rate: {results['success_rate']:.1f}%")

    if results.get('time_limit_exceeded', False):
        print("⏰ Quiz ended due to time limit!")

    if results['success_rate'] >= 90:
        print("🏆 Outstanding performance!")
    elif results['success_rate'] >= 80:
        print("🎉 Excellent work!")
    elif results['success_rate'] >= 60:
        print("👍 Good job!")
    elif results['success_rate'] >= 40:
        print("📚 Keep practicing!")
    else:
        print("💪 Don't give up! Practice makes perfect.")

    if level == 1 and results['success_rate'] >= 80:
        print("💡 You're doing great! Try Medium difficulty next time.")
    elif level == 2 and results['success_rate'] >= 80:
        print("💡 Ready for a challenge? Try Hard difficulty!")
    elif level == 2 and results['success_rate'] < 50:
        print("💡 Consider trying Easy difficulty to build confidence.")

    print(f"{'=' * 40}")


def update_word_statistics(quiz):
    if not quiz.answers:
        return

    for i, answer in enumerate(quiz.answers):
        if i < len(quiz.questions):
            question = quiz.questions[i]
            word_obj = question.get('word_object')
            if word_obj:
                if answer.get('is_correct', False):
                    word_obj.correct_answers += 1
                else:
                    word_obj.incorrect_answers += 1


def quiz_handler(vocabulary):
    """
    Complete quiz workflow with user interaction and difficulty levels.
    """
    if vocabulary.get_words_count() == 0:
        print("\n⚠️  The dictionary is empty!")
        print("Please add words before taking a quiz.")
        return False

    print(f"\n{'=' * 40}")
    print("START NEW QUIZ")
    print(f"{'=' * 40}")

    try:
        print(f"\nSelect difficulty level:")
        print("1. Easy - No time limit, first letter hints available")
        print("2. Medium - Timed (50 sec for 10 words), no hints")
        print("3. Hard - Strict timing (30 sec for 10 words), no hints")
        print(f"{'─' * 30}")

        while True:
            level_input = input("Choose difficulty (1-3): ").strip()
            if level_input in ['1', '2', '3']:
                level = int(level_input)
                break
            else:
                print("Please enter 1, 2, or 3")

        max_words = vocabulary.get_words_count()
        while True:
            try:
                count_input = input(f"\nNumber of words (1-{max_words}): ").strip()
                words_count = int(count_input)
                if 1 <= words_count <= max_words:
                    break
                else:
                    print(f"Please enter a number between 1 and {max_words}")
            except ValueError:
                print("Please enter a valid number")

        mode_options = ['word_to_translation', 'translation_to_word', 'mixed']
        mode_descriptions = {
            'word_to_translation': 'Word → Translation',
            'translation_to_word': 'Translation → Word',
            'mixed': 'Mixed (both directions)'
        }

        print("\nQuiz modes:")
        for i, mode in enumerate(mode_options, 1):
            print(f"  {i}. {mode_descriptions[mode]}")

        while True:
            mode_input = input(f"\nSelect mode (1-3): ").strip()

            if mode_input in ['1', '2', '3']:
                mode = mode_options[int(mode_input) - 1]
                break
            elif mode_input in mode_options:
                mode = mode_input
                break
            else:
                print("Please enter 1, 2, 3, or the mode name")

        print(f"\n{'─' * 30}")
        print("QUIZ SETTINGS:")
        print(f"Difficulty: {'Easy' if level == 1 else 'Medium' if level == 2 else 'Hard'}")
        print(f"Words: {words_count}")
        print(f"Mode: {mode_descriptions[mode]}")

        time_limit = get_time_limit(level, words_count)
        if time_limit > 0:
            print(f"Time limit: {format_time(time_limit)}")
        else:
            print("Time limit: Unlimited")

        confirm = input("\nStart quiz? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Quiz cancelled.")
            return False

        print(f"\n{'─' * 30}")

        quiz = create_quiz(vocabulary, words_count, mode)
        results = conduct_quiz(quiz, level)

        display_results(results, level)

        update_word_statistics(quiz)

        return True

    except NotEnoughWordsError as e:
        print(f"\n❌ Error: {e}")
        return False
    except ValueError as e:
        print(f"\n❌ Error: {e}")
        return False
    except KeyboardInterrupt:
        print(f"\n\n⏹️  Quiz interrupted by user.")
        return False
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        return False
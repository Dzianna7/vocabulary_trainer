import os
from src.vocabulary_trainer.core.models import Vocabulary
from src.vocabulary_trainer.dictionary.add_word import add_word
from src.vocabulary_trainer.dictionary.remove_word import remove_word
from src.vocabulary_trainer.dictionary.show_all_words import show_all_words
from src.vocabulary_trainer.dictionary.import_from_file import import_from_file
from src.vocabulary_trainer.testing.start_quiz import start_quiz
from src.vocabulary_trainer.testing.ask_question import get_current_question, get_question_text, submit_answer
from src.vocabulary_trainer.testing.calculate_score import calculate_score
from src.vocabulary_trainer.testing.test_difficulty import get_recommended_quiz_settings
from src.vocabulary_trainer.core.exceptions import WordAlreadyExistsError



def show_menu():
    """Показывает главное меню"""
    print("\n=== WordFlow - приложение для изучения новых слов ===")
    print("1. Добавить слово")
    print("2. Удалить слово")
    print("3. Показать все слова")
    print("4. Импорт слов из файла")
    print("5. Начать тестирование")
    print("6. Сохранить словарь")
    print("7. Статистика")
    print("0. Выход")


class VocabularyTrainerCLI:
    def __init__(self):
        self.vocabulary = Vocabulary()
        self.data_dir = "data/dictionaries"
        os.makedirs(self.data_dir, exist_ok=True)

    def save_vocabulary(self, filename: str = None) -> bool:
        """Сохраняет словарь в простом формате 'слово: перевод'"""
        if not filename:
            filename = f"{self.vocabulary.name}.txt"

        filepath = os.path.join(self.data_dir, filename)
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                for word in self.vocabulary.words.values():
                    f.write(f"{word.word}: {word.translation}\n")
            print(f"Словарь сохранен в {filepath}")
            return True
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
            return False

    def handle_add_word(self):
        """Обрабатывает добавление слова"""
        word = input("Введите слово: ").strip()
        translation = input("Введите перевод: ").strip()

        try:
            add_word(self.vocabulary, word, translation)
            print(f"Слово '{word}' добавлено в словарь")
        except (ValueError, WordAlreadyExistsError) as e:
            print(f"Ошибка: {e}")

    def handle_remove_word(self):
        """Обрабатывает удаление слова"""
        word = input("Введите слово для удаления: ").strip()

        try:
            if remove_word(self.vocabulary, word):
                print(f"Слово '{word}' удалено из словаря")
        except Exception as e:
            print(f"Ошибка: {e}")

    def handle_show_words(self):
        """Показывает все слова"""
        try:
            words = show_all_words(self.vocabulary)
            print(f"\n=== СЛОВАРЬ ({len(words)} слов) ===")
            for i, word in enumerate(words, 1):
                print(f"{i}. {word.word} - {word.translation}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def handle_import(self):
        """Обрабатывает импорт слов"""
        filepath = input("Введите путь к файлу: ").strip()

        try:
            count = import_from_file(self.vocabulary, filepath)
            print(f"Импортировано {count} слов")
        except Exception as e:
            print(f"Ошибка при импорте: {e}")

    def handle_quiz(self):
        """Запускает тестирование"""
        if self.vocabulary.get_words_count() == 0:
            print("Словарь пуст! Добавьте слова перед тестированием.")
            return

        # recommended settings according to number of words
        settings = get_recommended_quiz_settings(self.vocabulary)
        print(f"\nРекомендованные настройки (уровень {settings['difficulty_level']}):")
        print(f"Количество слов: {settings['recommended_word_count']}")
        print(f"Режим: {settings['mode']}")

        # requesting parameters from the user
        try:
            words_count = int(
                input(f"Количество слов (по умолчанию {settings['recommended_word_count']}): ") or settings[
                    'recommended_word_count'])
            mode = input(f"Режим (word_to_translation/translation_to_word/mixed, по умолчанию {settings['mode']}): ") or \
                   settings['mode']
        except ValueError:
            print("Неверный формат числа")
            return

        try:
            quiz_session = start_quiz(self.vocabulary, words_count, mode)
            print(f"\n=== НАЧАЛО ТЕСТИРОВАНИЯ ===")
            print(f"Режим: {mode}, Слов: {words_count}")

            while not quiz_session.is_completed():
                current_question = get_current_question(quiz_session)
                if current_question:
                    question_text = get_question_text(current_question)
                    user_answer = input(f"\n{question_text}: ")

                    is_correct = submit_answer(quiz_session, user_answer)
                    if is_correct:
                        print("✅ Правильно!")
                    else:
                        print(f"❌ Неправильно! Правильный ответ: {current_question['correct_answer']}")

            # showing results
            results = calculate_score(quiz_session)
            print(f"\n=== РЕЗУЛЬТАТЫ ===")
            print(f"Правильных ответов: {results['correct_answers']}/{results['total_questions']}")
            print(f"Успеваемость: {results['success_rate']:.1f}%")

        except Exception as e:
            print(f"Ошибка при тестировании: {e}")

    def handle_statistics(self):
        """Показывает статистику"""
        total_words = self.vocabulary.get_words_count()
        if total_words == 0:
            print("Словарь пуст")
            return

        total_correct = sum(word.correct_answers for word in self.vocabulary.get_all_words())
        total_incorrect = sum(word.incorrect_answers for word in self.vocabulary.get_all_words())

        print(f"\n=== СТАТИСТИКА ===")
        print(f"Всего слов: {total_words}")
        print(f"Правильных: {total_correct}")
        print(f"Неправильных: {total_incorrect}")

    def run(self):
        """Запускает главный цикл приложения"""
        print("Добро пожаловать в тренажер словарного запаса!")

        while True:
            show_menu()
            choice = input("\nВыберите действие: ").strip()

            if choice == '1':
                self.handle_add_word()
            elif choice == '2':
                self.handle_remove_word()
            elif choice == '3':
                self.handle_show_words()
            elif choice == '4':
                self.handle_import()
            elif choice == '5':
                self.handle_quiz()
            elif choice == '6':
                filename = input("Введите имя файла (по умолчанию: vocabulary.json): ").strip()
                self.save_vocabulary(filename or "vocabulary.json")
            elif choice == '7':
                self.handle_statistics()
            elif choice == '0':
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Попробуйте снова.")


def main():
    app = VocabularyTrainerCLI()
    app.run()


if __name__ == "__main__":
    main()
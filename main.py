from typing import Dict, List

from src.dictionary_management.add_word import add_word
from src.dictionary_management.import_from_file import import_from_file
from src.dictionary_management.remove_word import remove_word
from src.dictionary_management.show_all_words import show_all_words


def main():
    """
    Main function to run the Vocabulary Trainer application.
    """
    print("=" * 50)
    print("       🎯 VOCABULARY TRAINER")
    print("=" * 50)

    # the dictionary of words a person wants to add in the app (just an example)
    vocabulary = {
        "apple": "яблоко",
        "book": "книга",
        "computer": "компьютер",
        "house": "дом",
        "water": "вода"
    }

    print(f"📍 Текущий словарь: {len(vocabulary)} слов")
    # creating the context menu
    while True:
        print("\n📋 Главное меню:")
        print("1. Добавить слово")
        print("2. Удалить слово")
        print("3. Показать все слова")
        print("4. Начать тест")
        print("5. Импорт из файла")
        print("7. Выйти")

        choice = input("\nВыберите действие (1-7): ").strip()

        if choice == '1':
            # adding a word
            word = input("Введите английское слово: ").strip()
            translation = input("Введите перевод: ").strip()
            if add_word(vocabulary, word, translation): # just an example
                print(f"✅ Слово '{word}' добавлено!")
                print(f"📊 Теперь в словаре: {len(vocabulary)} слов")
            else:
                print(f"❌ Слово '{word}' уже существует!")

        elif choice == '2':
            # removing a word
            word = input("Введите слово для удаления: ").strip()
            if remove_word(vocabulary, word): # just an example
                print(f"✅ Слово '{word}' удалено!")
                print(f"📊 Теперь в словаре: {len(vocabulary)} слов")
            else:
                print(f"❌ Слово '{word}' не найдено!")

        elif choice == '3':
            # showing all the words
            words = show_all_words(vocabulary) # just an example
            if words:
                print(f"\n📚 Ваш словарь ({len(words)} слов):")
                for i, (eng, rus) in enumerate(words, 1):
                    print(f"{i}. {eng} - {rus}")
            else:
                print("📭 Словарь пуст!")

        elif choice == '4':
            # starting a test
            if not vocabulary:
                print("❌ Словарь пуст! Добавьте слова перед тестированием.")
                continue

            try:
                count = int(input(f"Сколько слов в тесте? (до {len(vocabulary)}): "))
                if count <= 0 or count > len(vocabulary):
                    print(f"❌ Введите число от 1 до {len(vocabulary)}")
                    continue

                print("Режимы: 1-en_to_ru, 2-ru_to_en, 3-mixed")
                mode_choice = input("Выберите режим (1-3): ")

                modes = {'1': 'en_to_ru', '2': 'ru_to_en', '3': 'mixed'}
                mode = modes.get(mode_choice, 'en_to_ru')

                print(f"\n🎯 Начинаем тест ({mode})...")
                print(f"📝 Будет задано {count} вопросов")
                # must be a start_quiz call and the logic of testing

            except ValueError:
                print("❌ Ошибка: введите число!")

        elif choice == '5':
            # importing from a file
            filename = input("Введите имя файла для импорта: ").strip()
            old_count = len(vocabulary)
            if import_from_file(vocabulary, filename): # just an example
                new_count = len(vocabulary)
                added_count = new_count - old_count
                print(f"📊 Теперь в словаре: {new_count} слов (+{added_count})")

        elif choice == '7':
            print("👋 До свидания!")
            break

        else:
            print("❌ Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()
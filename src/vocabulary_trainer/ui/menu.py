from src.vocabulary_trainer.core.models import Vocabulary
from src.vocabulary_trainer.dictionary.add_word import add_word
from src.vocabulary_trainer.dictionary.remove_word import remove_word
from src.vocabulary_trainer.dictionary.show_all_words import show_all_words
from src.vocabulary_trainer.testing.quiz_mode import quiz_handler


def show_menu():
    """
    Display the main menu options for the vocabulary trainer application.
    Shows all available actions the user can perform.
    """
    print("\n=== Welcome to WordFlow - Vocabulary Learning Application ===")
    print("1. Add word")
    print("2. Remove word")
    print("3. Show all words")
    print("4. Start quiz")
    print("0. Exit")


class VocabularyTrainerCLI:
    """
    Command-line interface for the vocabulary trainer application.
    """
    def __init__(self):
        self.vocabulary = Vocabulary()

    def run(self):
        while True:
            show_menu()
            choice = input("\nChoose an action: ").strip()

            if choice == '1':
                add_word(self.vocabulary)
            elif choice == '2':
                remove_word(self.vocabulary)
            elif choice == '3':
                show_all_words(self.vocabulary)
            elif choice == '4':
                quiz_handler(self.vocabulary)
            elif choice == '0':
                print("Goodbye! Have a nice day!")
                break
            else:
                print("Invalid choice. Please try again.")


from src.vocabulary_trainer.core.exceptions import WordNotFoundError

def remove_word(vocabulary):
    try:
        word = input("Enter word to remove: ").strip()

        if not word:
            print("Error: Word cannot be empty")
            return False

        if vocabulary.try_remove_word(word):
            print(f"Word '{word}' removed from dictionary")
            return True
        else:
            raise WordNotFoundError(f"Word '{word}' not found in dictionary")

    except WordNotFoundError as e:
        print(f"Error: {e}")
        return False
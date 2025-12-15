from src.vocabulary_trainer.core.exceptions import WordAlreadyExistsError

def add_word(vocabulary) -> bool:
    try:
        word = input("Enter word: ").strip()
        translation = input("Enter translation: ").strip()

        if not word or not translation:
            raise ValueError("A word or a translation must be provided")

        word = word.strip()
        translation = translation.strip()

        if not vocabulary.try_add_word(word, translation):
            raise WordAlreadyExistsError(f"The word '{word}' has already been added")

        print(f"Word '{word}' added to dictionary")
        return True

    except (ValueError, WordAlreadyExistsError) as e:
        print(f"Error: {e}")
        return False

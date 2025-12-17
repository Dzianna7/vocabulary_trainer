import tkinter as tk
from src.vocabulary_trainer.core.exceptions import WordAlreadyExistsError


def add_word(word_entry, translation_entry, vocabulary, result_label=None):
    try:
        word = word_entry.get().strip()
        translation = translation_entry.get().strip()

        if not word or not translation:
            if result_label:
                result_label.config(
                    text="Error: Both word and translation must be provided", fg="red"
                )
            return False

        if vocabulary.try_add_word(word, translation):
            word_entry.delete(0, tk.END)
            translation_entry.delete(0, tk.END)

            if result_label:
                result_label.config(
                    text=f"Word '{word}' added successfully!", fg="green"
                )
            return True
        else:
            raise WordAlreadyExistsError(f"Word '{word}' already exists in dictionary")

    except WordAlreadyExistsError as e:
        if result_label:
            result_label.config(text=f"Error: {e}", fg="red")
        return False

    except Exception as e:
        if result_label:
            result_label.config(text=f"Unexpected error: {e}", fg="red")
        print(f"Error adding word: {e}")
        return False

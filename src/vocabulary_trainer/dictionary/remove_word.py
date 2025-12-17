import tkinter as tk
from src.vocabulary_trainer.core.exceptions import WordNotFoundError


def remove_word(word_entry, vocabulary, result_label=None):
    try:
        word = word_entry.get().strip()

        if not word:
            if result_label:
                result_label.config(text="Error: Word cannot be empty", fg="red")
            return False

        if vocabulary.try_remove_word(word):
            word_entry.delete(0, tk.END)

            if result_label:
                result_label.config(
                    text=f"Word '{word}' removed successfully!", fg="green"
                )
            return True
        else:
            raise WordNotFoundError(f"Word '{word}' not found in dictionary")

    except WordNotFoundError as e:
        if result_label:
            result_label.config(text=f"Error: {e}", fg="red")
        return False

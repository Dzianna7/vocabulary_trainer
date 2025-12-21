# Нет докстрингов, импорты не отсортированы

import tkinter as tk
from typing import Optional  # Такая типизация устарела.
from src.vocabulary_trainer.core.models import Vocabulary  # Неправильные импорты. Все из-за того, что вы не заполнили `__init__.py`
from src.vocabulary_trainer.core.exceptions import WordNotFoundError


def remove_word(
    word_entry: tk.Entry,
    vocabulary: Vocabulary,
    result_label: Optional[tk.Label] = None
) -> bool:
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

import tkinter as tk
from typing import Optional, List
from src.vocabulary_trainer.core.models import Vocabulary, Word


def show_all_words(
    vocabulary: Vocabulary,
    text_widget: Optional[tk.Text] = None,
    result_label: Optional[tk.Label] = None
) -> Optional[List[Word]]:
    try:
        words = vocabulary.try_show_all_words()

        word_list = [
            f"{i + 1}. {word.word} - {word.translation}" for i, word in enumerate(words)
        ]
        formatted_text = f"Dictionary contains {len(words)} words:\n\n" + "\n".join(
            word_list
        )

        if text_widget:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, formatted_text)
            text_widget.config(state=tk.DISABLED)

        if result_label:
            result_label.config(
                text=f"Successfully loaded {len(words)} words", fg="green"
            )

        return words

    except Exception as e:
        error_msg = f"Error: {e}"
        if text_widget:
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, error_msg)
            text_widget.config(fg="red", state=tk.DISABLED)

        if result_label:
            result_label.config(text=error_msg, fg="red")
        return None

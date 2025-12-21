# Нет докстрингов, импорты не отсортированы

import tkinter as tk
from tkinter import scrolledtext, messagebox
import time
from src.vocabulary_trainer.core.models import Vocabulary, QuizSession  # Неправильные импорты.
from src.vocabulary_trainer.dictionary.add_word import add_word
from src.vocabulary_trainer.dictionary.remove_word import remove_word
from src.vocabulary_trainer.dictionary.show_all_words import show_all_words
from src.vocabulary_trainer.quiz_session.quiz_mode import (
    create_quiz,
    update_word_statistics,
)
from src.vocabulary_trainer.quiz_session.test_difficulty import (
    get_time_limit,
    format_time,
    get_first_letter_hint,
)
from src.vocabulary_trainer.quiz_session.ask_question import (
    get_current_question,
    get_question_text,
    submit_answer,
)


class VocabularyTrainerGUI:
    def __init__(self, master: tk.Tk):
        self.master = master
        self.vocabulary = Vocabulary()
        self.create_main_menu()

    def create_main_menu(self) -> None:
        tk.Label(
            self.master, text="Vocabulary Trainer", font=("Arial", 16, "bold")
        ).pack(pady=20)

        frame = tk.Frame(self.master)
        frame.pack(pady=30)

        buttons = [
            ("➕ Add Word", self.add_word_window),
            ("➖ Remove Word", self.remove_word_window),
            ("📋 Show All Words", self.show_words_window),
            ("📝 Start Quiz", self.start_quiz),
        ]

        for i, (text, cmd) in enumerate(buttons):
            btn = tk.Button(
                frame, text=text, command=cmd, width=20, height=2, font=("Arial", 10)
            )
            btn.grid(row=i // 2, column=i % 2, padx=10, pady=10)

        tk.Button(
            self.master,
            text="Exit",
            command=self.master.quit,
            width=15,
            height=1,
            font=("Arial", 10),
        ).pack(pady=20)

    def add_word_window(self) -> None:
        window = tk.Toplevel(self.master)
        window.title("Add New Word")
        window.geometry("400x250")

        tk.Label(window, text="Add New Word", font=("Arial", 14)).pack(pady=15)

        frame = tk.Frame(window)
        frame.pack(pady=10)

        tk.Label(frame, text="Word:").grid(row=0, column=0, sticky="w", pady=5)
        word_entry = tk.Entry(frame, width=25, font=("Arial", 10))
        word_entry.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(frame, text="Translation:").grid(row=1, column=0, sticky="w", pady=5)
        trans_entry = tk.Entry(frame, width=25, font=("Arial", 10))
        trans_entry.grid(row=1, column=1, pady=5, padx=10)

        result_label = tk.Label(window, text="", fg="green", font=("Arial", 10))
        result_label.pack(pady=5)

        btn_frame = tk.Frame(window)
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame,
            text="Add",
            command=lambda: add_word(
                word_entry, trans_entry, self.vocabulary, result_label
            ),
            width=10,
            font=("Arial", 10),
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame,
            text="Close",
            command=window.destroy,
            width=10,
            font=("Arial", 10),
        ).grid(row=0, column=1, padx=5)

        word_entry.focus()

    def remove_word_window(self) -> None:
        window = tk.Toplevel(self.master)
        window.title("Remove Word")
        window.geometry("400x180")

        tk.Label(window, text="Remove Word", font=("Arial", 14)).pack(pady=15)

        tk.Label(window, text="Enter word to remove:").pack(pady=5)

        word_entry = tk.Entry(window, width=25, font=("Arial", 10))
        word_entry.pack(pady=5)

        result_label = tk.Label(window, text="", font=("Arial", 10))
        result_label.pack(pady=5)

        btn_frame = tk.Frame(window)
        btn_frame.pack(pady=10)

        tk.Button(
            btn_frame,
            text="Remove",
            command=lambda: remove_word(word_entry, self.vocabulary, result_label),
            width=10,
            font=("Arial", 10),
        ).grid(row=0, column=0, padx=5)
        tk.Button(
            btn_frame,
            text="Close",
            command=window.destroy,
            width=10,
            font=("Arial", 10),
        ).grid(row=0, column=1, padx=5)

        word_entry.focus()

    def show_words_window(self) -> None:
        window = tk.Toplevel(self.master)
        window.title("All Words")
        window.geometry("500x350")

        tk.Label(window, text="All Words", font=("Arial", 14)).pack(pady=10)

        text_area = scrolledtext.ScrolledText(
            window, wrap=tk.WORD, width=50, height=12, font=("Arial", 10)
        )
        text_area.pack(padx=10, pady=10, fill="both", expand=True)

        result_label = tk.Label(window, text="", font=("Arial", 10))
        result_label.pack()

        tk.Button(
            window, text="Close", command=window.destroy, width=10, font=("Arial", 10)
        ).pack(pady=10)

        show_all_words(self.vocabulary, text_area, result_label)

    def start_quiz(self) -> None:
        if self.vocabulary.get_words_count() == 0:
            messagebox.showwarning(
                "Empty Dictionary", "Add words before taking a quiz."
            )
            return

        settings_window = tk.Toplevel(self.master)
        settings_window.title("Quiz Settings")
        settings_window.geometry("400x350")

        tk.Label(settings_window, text="Quiz Settings", font=("Arial", 14)).pack(
            pady=10
        )

        frame = tk.Frame(settings_window, padx=20)
        frame.pack()

        tk.Label(frame, text="Difficulty:").grid(row=0, column=0, sticky="w", pady=10)
        difficulty = tk.IntVar(value=1)

        difficulties = [
            ("Easy (no time limit, hints)", 1),
            ("Medium (timed)", 2),
            ("Hard (strict timing)", 3),
        ]

        for i, (text, val) in enumerate(difficulties):
            tk.Radiobutton(frame, text=text, variable=difficulty, value=val).grid(
                row=i, column=1, sticky="w"
            )

        tk.Label(frame, text="Number of words:").grid(
            row=4, column=0, sticky="w", pady=10
        )

        max_words = min(20, self.vocabulary.get_words_count())
        words_count = tk.IntVar(value=min(5, max_words))

        tk.Scale(
            frame,
            from_=1,
            to=max_words,
            variable=words_count,
            orient="horizontal",
            length=200,
        ).grid(row=4, column=1, pady=5)

        tk.Label(frame, text="Mode:").grid(row=5, column=0, sticky="w", pady=10)
        mode = tk.StringVar(value="mixed")

        modes = [
            ("Word → Translation", "word_to_translation"),
            ("Translation → Word", "translation_to_word"),
            ("Mixed", "mixed"),
        ]

        for i, (text, val) in enumerate(modes):
            tk.Radiobutton(frame, text=text, variable=mode, value=val).grid(
                row=5 + i, column=1, sticky="w"
            )

        btn_frame = tk.Frame(settings_window)
        btn_frame.pack(pady=20)

        def start() -> None:
            settings_window.destroy()
            self.run_quiz(difficulty.get(), words_count.get(), mode.get())

        tk.Button(btn_frame, text="Start", command=start, width=10).pack(
            side="left", padx=5
        )
        tk.Button(
            btn_frame, text="Cancel", command=settings_window.destroy, width=10
        ).pack(side="left", padx=5)

    def run_quiz(self, level: int, words_count: int, mode: str) -> None:
        try:
            quiz = create_quiz(self.vocabulary, words_count, mode)
            self.quiz_window(quiz, level)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def quiz_window(self, quiz: QuizSession, level: int) -> None:
        window = tk.Toplevel(self.master)
        window.title("Vocabulary Quiz")
        window.geometry("500x450")

        current_index = 0
        correct_answers = 0
        start_time = time.time()
        time_limit = get_time_limit(level, quiz.words_count)
        hint_used = False
        current_question = None

        top_frame = tk.Frame(window)
        top_frame.pack(fill="x", padx=10, pady=5)

        progress_label = tk.Label(
            top_frame, text=f"Question 1/{quiz.words_count}", font=("Arial", 12)
        )
        progress_label.pack(side="left")

        timer_label = tk.Label(top_frame, text="", font=("Arial", 12))
        timer_label.pack(side="right")

        def update_timer() -> None:
            if time_limit <= 0:
                return

            elapsed = time.time() - start_time
            remaining = max(0, time_limit - int(elapsed))

            if remaining > 0:
                timer_label.config(text=f"Time: {format_time(remaining)}")
                timer_label.after(1000, update_timer)  # Parameter 'args' unfilled, expected '*tuple[]'
            else:
                timer_label.config(text="TIME'S UP!")
                end_quiz()

        if time_limit > 0:
            update_timer()

        main_frame = tk.Frame(window, padx=20, pady=10)
        main_frame.pack(fill="both", expand=True)

        question_label = tk.Label(main_frame, text="", font=("Arial", 14))
        question_label.pack(pady=20)

        tk.Label(main_frame, text="Your answer:").pack()

        answer_entry = tk.Entry(main_frame, font=("Arial", 12), width=30)
        answer_entry.pack(pady=10)

        hint_button = None
        if level == 1:
            hint_button = tk.Button(main_frame, text="Get Hint")
            hint_button.pack(pady=5)

        btn_frame = tk.Frame(window)
        btn_frame.pack(pady=10)

        def next_question() -> None:
            nonlocal current_index, hint_used
            current_index += 1
            quiz.current_question_index = current_index
            hint_used = False
            show_question()

        def check_answer() -> None:
            answer = answer_entry.get().strip()
            if not answer:
                return

            if submit_answer(quiz, answer):
                nonlocal correct_answers
                correct_answers += 1

            next_question()

        def show_question() -> None:
            nonlocal hint_used, current_question
            if current_index >= len(quiz.questions):
                end_quiz()
                return

            question = get_current_question(quiz)
            current_question = question

            progress_label.config(
                text=f"Question {current_index + 1}/{quiz.words_count}"
            )
            question_label.config(text=get_question_text(question))
            answer_entry.delete(0, tk.END)
            answer_entry.focus()

            if hint_button:
                hint_button.config(state="normal", text="Get Hint")
            hint_used = False

        def show_hint() -> None:
            nonlocal hint_used, current_question

            if (
                hint_used
                or not current_question
                or not isinstance(current_question, dict)
                or "word_object" not in current_question
                or "type" not in current_question
            ):
                return

            word_obj = current_question["word_object"]
            question_type = current_question["type"]

            if not word_obj:
                return

            if hint_button:
                hint_button.config(state="disabled", text="Hint used")

            hint_used = True

            hint_text = get_first_letter_hint(word_obj, question_type)
            messagebox.showinfo("Hint", hint_text)

        def end_quiz() -> None:
            update_word_statistics(quiz)

            total = len(quiz.questions)
            score = (correct_answers / total * 100) if total > 0 else 0

            message = "Quiz finished!\n\n"
            message += f"Questions: {total}\n"
            message += f"Correct: {correct_answers}\n"
            message += f"Score: {score:.1f}%\n\n"

            if score >= 90:
                message += "🏆 Outstanding performance!"
            elif score >= 80:
                message += "🎉 Excellent work!"
            elif score >= 60:
                message += "👍 Good job!"
            elif score >= 40:
                message += "📚 Keep practicing!"
            else:
                message += "💪 Don't give up! Practice makes perfect."

            messagebox.showinfo("Quiz Results", message)
            window.destroy()

        if hint_button:
            hint_button.config(command=show_hint)

        tk.Button(btn_frame, text="Submit", command=check_answer, width=10).pack(
            side="left", padx=5
        )
        tk.Button(btn_frame, text="Skip", command=next_question, width=10).pack(
            side="left", padx=5
        )

        answer_entry.bind("<Return>", lambda e: check_answer())
        show_question()

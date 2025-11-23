from typing import Dict


class Word:
    def __init__(self, word: str, translation: str):
        self.word = word
        self.translation = translation
        self.correct_answers = 0
        self.incorrect_answers = 0
        self.last_tested = None

    def mark_correct(self) -> None:
        pass
    # in immediate_answers.py

    def mark_incorrect(self) -> None:
        pass
    # in immediate_answers.py


class Vocabulary:
    def __init__(self):
        self.words = {}

    def add_word(self, word: str, translation: str) -> bool:
        pass
    # in add_word.py

    def remove_word(self, word: str, translation: str) -> bool:
        pass
    # in remove_word.py

    def show_all_words(self) -> bool:
        pass
    # in show_all_words.py

    def import_word(self, word: str, translation: str) -> bool:
        pass
    # in import words.py


class QuizSession:
    def __init__(self, words_count: int, mode: str, vocabulary: Vocabulary):
        self.words_count = words_count
        self.mode = mode
        self.vocabulary = vocabulary
        self.questions = []
        self.answers = []

    def start_quiz(self, words_count: int, mode: str, vocabulary: Vocabulary):
        pass
    # in start_quiz.py

    def ask_question(self, word: str, translation: str, user_answer: str) -> bool:
        pass
    # in ask_question.py

    def mark_correct(self) -> None:
        pass
    # in immediate_answers.py

    def mark_incorrect(self) -> None:
        pass
    # in immediate_answers.py

    def get_difficulty_preset(self) -> int:
        pass
    # in test_difficulty.py

    def calculate_score(self, session: QuizSession) -> Dict:
        pass
    # in calculate_score.py

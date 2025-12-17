from typing import Dict, List


class Word:
    def __init__(self, word, translation):
        self.word = word
        self.translation = translation
        self.correct_answers = 0
        self.incorrect_answers = 0

    def get_success_rate(self):
        total = self.correct_answers + self.incorrect_answers
        return self.correct_answers / total if total > 0 else 0.0


class Vocabulary:
    def __init__(self):
        self.words: Dict[str, Word] = {}

    def try_add_word(self, word, translation):
        if word.lower() in self.words:
            return False
        self.words[word.lower()] = Word(word, translation)
        return True

    def try_remove_word(self, word):
        if word.lower() in self.words:
            del self.words[word.lower()]
            return True
        return False

    def try_show_all_words(self):
        return list(self.words.values())

    def get_words_count(self):
        return len(self.words)

    def get_words_for_quiz(self, count):
        if not self.words:
            return []

        all_words = list(self.words.values())
        all_words.sort(key=lambda x: x.get_success_rate())
        return all_words[: min(count, len(all_words))]


class QuizSession:
    def __init__(self, words_count, mode, vocabulary):
        self.words_count = words_count
        self.mode = mode
        self.vocabulary = vocabulary
        self.questions: List[Dict] = []
        self.answers: List[Dict] = []
        self.current_question_index = 0

    def is_completed(self):
        return self.current_question_index >= len(self.questions)

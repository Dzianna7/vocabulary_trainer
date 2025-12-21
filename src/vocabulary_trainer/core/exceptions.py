# Это что такое? Кастомные исключения мы делаем, если хотим добавить кастомное поведение. А вы просто создали заглушки.
# Похоже на недописанный код. Такое чаще всего нельзя допускать в production

class WordAlreadyExistsError(Exception):
    pass


class WordNotFoundError(Exception):
    pass


class NotEnoughWordsError(Exception):
    pass

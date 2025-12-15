def get_time_limit(level: int, words_count: int) -> int:
    """
    Calculate time limit based on difficulty level and number of words.
    """
    if level == 1:  # Easy - no time limit
        return 0

    if level == 2:  # Medium - 50 seconds for 10 words, 5 seconds per word
        base_time = 50
        base_words = 10
        seconds_per_word = 5

        if words_count <= base_words:
            return words_count * seconds_per_word
        else:
            return base_time + (words_count - base_words) * seconds_per_word

    if level == 3:  # Hard - 30 seconds for 10 words, 3 seconds per word
        base_time = 30
        base_words = 10
        seconds_per_word = 3

        if words_count <= base_words:
            return words_count * seconds_per_word
        else:
            return base_time + (words_count - base_words) * seconds_per_word

    return 0


def format_time(seconds: int) -> str:
    if seconds == 0:
        return "Unlimited"

    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"


def get_first_letter_hint(word_obj, question_type: str) -> str:
    if question_type == 'word_to_translation':
        if word_obj.translation and len(word_obj.translation) > 0:
            return f"First letter of translation: '{word_obj.translation[0]}'"
    else:
        if word_obj.word and len(word_obj.word) > 0:
            return f"First letter of word: '{word_obj.word[0]}'"

    return "No hint available"

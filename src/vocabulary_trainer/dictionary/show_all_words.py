def show_all_words(vocabulary):
    try:
        words = vocabulary.try_show_all_words()
        if not words:
            raise ValueError("The vocabulary is empty")

        print(f"\n=== DICTIONARY ({len(words)} words) ===")
        for i, word in enumerate(words, 1):
            print(f"{i}. {word.word} - {word.translation}")

        return words

    except ValueError as e:
        print(f"Error: {e}")
        return None
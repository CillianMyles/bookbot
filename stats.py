def count_number_of_words_in_text(text):
    words = text.split()
    return len(words)

def count_characters_in_text(text):
    counts = {}
    for i in range(len(text)):
        char = text[i].lower()
        if char == '\ufeff':  # skip BOM
            continue
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    return counts

def sort_character_counts(counts):
    return counts.sort(reverse=True, key=_sort_on)

def _sort_on(items):
    return items["num"]

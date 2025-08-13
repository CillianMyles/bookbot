import sys
from stats import count_characters_in_text, count_number_of_words_in_text, sort_character_counts

def main():
    args = sys.argv
    args.remove("main.py")
    if len(args) != 1:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book = args[0]
    print(f"Analyzing book found at {book}")
    text = get_book_text(book)
    print("----------- Word Count ----------")
    word_count = count_number_of_words_in_text(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_count = count_characters_in_text(text)
    sorted_counts = sort_character_counts(character_count)
    for count in sorted_counts:
        print(f"{count['char']}: {count['num']}")
    print("============= END ===============")

def get_book_text(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Book not found. Please check the file path."

main()

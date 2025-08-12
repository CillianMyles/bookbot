from stats import count_characters_in_text, count_number_of_words_in_text

def main():
    print("============ BOOKBOT ============")
    book = "books/frankenstein.txt"
    print(f"Analyzing book found at {book}")
    text = get_book_text(book)
    print("----------- Word Count ----------")
    word_count = count_number_of_words_in_text(text)
    print(f"Found {word_count} total words")
    character_count = count_characters_in_text(text)
    print("--------- Character Count -------")
    print(character_count)

def get_book_text(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Book not found. Please check the file path."

main()

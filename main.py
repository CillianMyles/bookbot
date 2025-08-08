def main():
    text = get_book_text("books/frankenstein.txt")
    words = count_number_of_words_in(text)
    print(f"{words} words found in the document")

def get_book_text(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Book not found. Please check the file path."
    
def count_number_of_words_in(text):
    return len(text.split())

main()

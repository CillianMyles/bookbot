def main():
    print(get_book_text("books/frankenstein.txt"))

def get_book_text(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Book not found. Please check the file path."

main()

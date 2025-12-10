from stats import num_words, get_num_letters, sorted_letter_counts
import sys

def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if sys.argv.__len__() == 2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(book_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print( "----------- Word Count ----------")
    print(f'Found {num_words(book_text)} total words')
    letters_count = get_num_letters(book_text)
    letters_count = sorted_letter_counts(letters_count)
    print("--------- Character Count -------")
    for letter in letters_count:
        print(f'{letter["char"]}: {letter["num"]}')
    print("============= END ===============")
    
main()
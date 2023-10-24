def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_count = count_letters(text)
    get_report(book_path, num_words, letters_count)


def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letter_count = {}
    lower_text = text.lower()

    for letter in lower_text:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    return letter_count


def get_report(path, num_words, letters_count):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")

    sorted_list = sorted(letters_count.items(),
                         key=lambda x: x[1], reverse=True)

    for char, frequency in sorted_list:
        if char.isalpha():
            print(f"The '{char}' character was found {frequency} times")

    print("--- End report ---")


main()

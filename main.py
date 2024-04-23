def split_book(book):
    word_list = book.replace("\n", " ").split(" ")
    return word_list

def count_words(split_book):
    count = 0
    for word in split_book:
        if word != "":
            count = count + 1
    return count

def sort_on(tuple):
    return tuple[1]

def count_letters(book):
    letter_count_dict = {}
    book = book.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        letter_count_dict[letter] = book.count(letter)
    
    letter_count_list = list(letter_count_dict.items())
    letter_count_list.sort(reverse=True, key=sort_on)  
    return letter_count_list


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        split_file = split_book(file_contents)
        letter_count = count_letters(file_contents)
    
    print(f"{count_words(split_file)} words found in opened file")
    for tuple in letter_count:
        print(f"The letter {tuple[0]} has been used {tuple[1]} times")


main()
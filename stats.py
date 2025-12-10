def num_words(text):
    words = text.split()
    return len(words)

def get_num_letters(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def sorted_letter_counts(letter_counts):
    sorted_list = []
    for count in letter_counts:
        sorted_list.append({"char": count, "num": letter_counts[count]})
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
        
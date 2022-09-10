def print_upper_words(words):
    """" Print capitalized word from list that starts with e or E """

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())



print_upper_words(["hello","elephant","icecream", "earth", "Eat"])



def print_upper_words2(words, must_start_with):
    """" Print capitalized word from list that starts with specified letter in second argument """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter.upper()) or word.startswith(letter.lower()):
                print(word.upper())

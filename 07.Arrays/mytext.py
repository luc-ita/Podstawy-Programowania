def number_of_words(text):
    end_word = text.split()
    return len(end_word)

def ordered(text):
    end_word = text.split()
    return sorted(end_word, key=len, reverse=True)

def alpha(text):
    end_word = text.split()
    return sorted(end_word)

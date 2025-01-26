import json

paragraph = "cat dog mouse cat rat cat mouse"


def word_count(paragraph):
    words = paragraph.split(' ')
    word_count = {w: 0 for w in set(words)}
    for word in words:
        word_count[word] += 1
    return word_count



print(json.dumps(word_count(paragraph), indent=4))

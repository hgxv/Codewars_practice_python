def spin_words(sentence):
    result = ""
    text = sentence.split()
    for index, word in enumerate(text):
        if len(word) > 4:
            text[index] = word[::-1]
    return ' '.join(text)
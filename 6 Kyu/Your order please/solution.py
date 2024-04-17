def order(sentence):
    words = sentence.split()
    result = ['' for word in words]
    for index, word in enumerate(words, 1):
        for letter in word:
            try:
                result[int(letter) - 1] = words[index - 1]
            except:
                pass
            
    return ' '.join(result)
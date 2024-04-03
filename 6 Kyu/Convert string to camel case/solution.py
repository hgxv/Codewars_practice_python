def to_camel_case(text):
    result = ""
    for index, char in enumerate(text):
        if char != "-" and char != "_":
            if text[index - 1] == "-" or text[index - 1] == "_":
                result += char.upper()
                continue
            result += char
    return result
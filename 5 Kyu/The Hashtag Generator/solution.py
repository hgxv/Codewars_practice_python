def generate_hashtag(s):
    s = s.split()
    
    result = "#"
    for index, word in enumerate(s):
        s[index] = word.lower()
        s[index] = word.capitalize()
        
    result += ("".join(s))
    
    if len(result) > 140 or result == "#":
        return False
    return result

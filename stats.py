
def word_count( contents ):
    number_words = len( contents.split() )

    return number_words

def char_count(contents):
    char_dict = {}
    for charb in contents:
        char = charb.lower() 
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict
def to_jaden_case(string):
    words = string.split()
    upper = ' '.join(word.capitalize() for word in words)
    print(upper)
    return upper

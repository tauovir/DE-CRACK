
def get_length(text):
    """
    return the length of last word of text
    example: text= 'Country is India'
    Output:  length : 5
    example: text= 'I love to eat Banana'
    Output:  length : 6
    """
    pass

def imp_get_length(text):
    """
    return the length of last word of text
    example: text= 'Country is India'
    Output:  length : 5
    example: text= 'I love to eat Banana'
    Output:  length : 6
    """
    return len(text.split(" ")[-1])
    
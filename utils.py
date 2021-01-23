def raw(text):
    """Get all stuff after the prefix"""
    return " ".join([word for word in text.split(' ')[1:] if word])


def getargs(text):
    """Get arguments separated by space"""
    return text.split()[1:]

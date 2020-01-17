def most_e(*args):
    """
    From arbitrary number of strings, pick up the string with the most
    occurrences of letter 'e' (case insensitive).
    :param args: (string) arbitrary number of strings
    :return: (string ) string with the most occurrences of the letter
    'e' (upper or lower)
    """
    if not args:
        return None
    return max(args, key=lambda string: string.lower().count('e'))

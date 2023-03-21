def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
# index 0 of phrase. upper 
    return phrase[0].upper() + phrase[1:]
    
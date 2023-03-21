def flip_case(phrase, to_swap):
    str = ""
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    # if it contain letter
    #if letter is 
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            str += letter.swapcase()
        else:
            str += letter 
    return str

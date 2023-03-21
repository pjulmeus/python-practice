def multiple_letter_count(phrase):
    dict = {}
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # iterate each letter nd creates a dictionary 
    for letter in phrase:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] =1
    return dict
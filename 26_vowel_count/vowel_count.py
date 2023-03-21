def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
#  iterate
    vowel = set('aeiou')
    phraseLow = phrase.lower()
    dict = {}
    for letter in phraseLow:      
        if letter in vowel: 
            print(letter)
            if dict[letter]:
                dict[letter] += 1
            else: 
                dict[letter] = 1
    return dict 
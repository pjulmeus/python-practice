def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    #  make the list a set 
    dict1 = {}
    dict2 = {}
    str1 = (str(num1))
    str2 = (str(num2))
    set1 = (set(str1))
    set2 = set(str2)
    

    if len(str1) is not len(str2): 
        return False
    else:
        for n1 in set1:
            if dict1[n1] in dict1:
                dict1[n1] += 1
            else:
                dict1[n1] = 1
    return dict

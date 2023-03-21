def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    #  if in 
    # irterate through the sought to see if its in the collection 
    # check the type 
    
    if start is not None:
        if type(collection) == str or  type(collection) == list or type(collection) == tuple:  
            start_collection = (collection[start::])
            print(start_collection)
            if sought in start_collection:
                return True
        if type(collection) == dict:        
            if sought in collection.values() :
                return True 
        if type(collection) == set or type(collection) == tuple:
            if sought in collection:
                return True 
    elif start == None:
        if type(collection) == dict:
            if sought in collection.values():
                return True 
        else:
            if sought in collection:
                return True
    return False
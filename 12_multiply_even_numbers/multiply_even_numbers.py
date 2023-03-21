def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    product = 1
    for num in nums:
        if num % 2 == 0:
            print(num)
            product *= num
    return product

    # create a totel =1 
    #  iterate and pull anything with the module of 2 
    # multiply number by product 
    #  return product

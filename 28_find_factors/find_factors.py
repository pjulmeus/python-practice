def find_factors(num): 
    n = 1
    lst = []
    while (n <= num) :   
        print(n)
        if num % n == 0:
            lst.append(n)
        n += 1                  
    return lst

 # """Find factors of num, in increasing order.

    # >>> find_factors(10)
    # [1, 2, 5, 10]

    # >>> find_factors(11)
    # [1, 11]

    # >>> find_factors(111)
    # [1, 3, 37, 111]

    # >>> find_factors(321421)
    # [1, 293, 1097, 321421]
    # """
#  lets use while iterate through a range 
#  factar are anything that is divisible by the num 
#  if num is divisible by n 
# then append n
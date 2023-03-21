def sum_range(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range(nums)
        10

        >>> sum_range(nums, 1)
        9

        >>> sum_range(nums, end=2)
        6

        >>> sum_range(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range(nums, 1, 99)
        9
    """
    sum = 0
    print(len(nums))
    print(end)
    if start == 0:
        if end == None:
            for num in nums: 
                sum += num
        else:
            if end <= len(nums):
                end_nums = (nums[:end+1:]) 
                print(end_nums)
                for end_n in end_nums:
                    sum += end_n
    if start > 0:
        if end == None:
            start_nums = (nums[start::]) 
            for start_n in start_nums:
                sum += start_n
        else:
            if end > len(nums):
                start_nums = nums[start::]
                for n in start_nums:
                    sum += n
            if end <= len(nums):
                full_nums = nums[start:end+1:]
                print(full_nums)
                for full_n in full_nums:
                    sum += full_n  
    return sum 

# sum iterate the list 
# if list has a start [start::] and not end
# if list has a start and end
# if list has an end but start 

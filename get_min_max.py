def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.
    Args: ints(list): list of integers containing one or more integers
    """
    ## Corner case
    if len(ints) < 1:
        return (None, None)

    # Assign first number of an array to both min and max
    min_num = ints[0]
    max_num = ints[0]

    # Traverse once through an array compare each element with min, max
    # reassign min, max based on comparison
    for num in ints:
        if num < min_num:
            min_num = num

        if num > max_num:
            max_num = num

    return (min_num, max_num)

        

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 1000)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 999) == get_min_max(l)) else "Fail")

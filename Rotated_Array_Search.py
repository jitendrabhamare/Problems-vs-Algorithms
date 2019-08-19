# Search in a Rotated Sorted Array
# # Author: Jitendra Bhamare

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Args: input_list(array), number(int): Input array to search and the target
    Returns: int: Index or -1
    """
    # Corner case conditions
    if len(input_list) == 0:
        return -1
    elif len(input_list) == 1:
        if input_list[0] == number:
            return 0
        return -1
    else:
        #Call a recursive helper function
        return rot_search_helper(0, len(input_list)-1, input_list, number)

def rot_search_helper(first_index, last_index, array, number):
    """ Performs binary search. 
        the key logic is to find either left half or right half of an array where
        a number potentially can lie. 
    """
    # Return a number-index immediately if it's first or last 
    if array[first_index] == number:
        return first_index
    elif array[last_index] == number:
        return last_index
    
    # Else find it's in left half or right half of a rotated array
    else:
        if first_index == last_index:
            return -1
        mid_index = (first_index + last_index) //2
        # check mid value
        if array[mid_index] == number:
            return mid_index
        # check if number in left half
        elif (array[first_index] < number < array[mid_index]) \
        or (number > array[first_index] and number > array[mid_index]) and number > array[last_index]:
            return rot_search_helper(first_index, mid_index-1, array, number)
        # if number is in right array
        elif (number <= array[last_index]):
            return rot_search_helper(mid_index+1, last_index, array, number)
        else:
            return -1

    

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


## Test cases
def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

## Edge cases
test_function([[], 6]) # empty array
test_function([[6], 6]) # Array with one element
test_function([[11], 6]) # array with one element
test_function([[1, 2, 3, 4, 6, 7, 8, 9, 10], 6]) # Array with no rotation


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

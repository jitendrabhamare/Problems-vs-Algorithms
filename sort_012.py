def sort_012(list_012):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    Args: list_012(list): List to be sorted
    """
    next_pos_0 = 0
    next_pos_2 = len(list_012) - 1

    front_index = 0

    while front_index <= next_pos_2:
        if list_012[front_index] == 0:
            list_012[front_index] = list_012[next_pos_0]
            list_012[next_pos_0] = 0
            next_pos_0 += 1
            front_index += 1
        elif list_012[front_index] == 2:           
            list_012[front_index] = list_012[next_pos_2] 
            list_012[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            front_index += 1

    return list_012


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

## Edge cases
test_function([]) # Empty Array
test_function([0]) # Array with one element
test_function([2, 0]) # Array with 2 elements
test_function([2, 1, 0]) # Array with 3 elements


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.
    Args: input_list(list): Input List
    Returns: (int),(int): Two maximum sums
    """
    ## Corner cases:
    if len(input_list) == 0:
        return [0, 0]
    elif len(input_list) == 1:
        return [input_list[0], 0]

    # Sort an array using merge-sort
    sorted_list = merge_sort(input_list)

    # Create two empty array and pop largest number from an sorted_list 
    # and push into each empty array one by one
    # This also ensures that the number of digits in both the numbers cannot differ by more than 1
    first_num_list = list()
    second_num_list = list()
    
    while sorted_list:
        first_num_list.append(sorted_list.pop())
        if not sorted_list:
            break
        second_num_list.append(sorted_list.pop())

    first_num = int("".join(str(i) for i in first_num_list))
    second_num = int("".join(str(i) for i in second_num_list))
    
    # Create an output array of two nums
    out_list = []
    out_list.append(first_num)
    out_list.append(second_num)
    return out_list

def merge_sort(array):

    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged_array = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged_array.append(right[right_index])
            right_index += 1
        else:
            merged_array.append(left[left_index])
            left_index += 1

    merged_array += left[left_index:]
    merged_array += right[right_index:]
        
    return merged_array


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    print("output: {}".format(output))
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

## Edge case
test_function([[], [0, 0]]) # empty input array
test_function([[5], [5, 0]]) # input array with just one element
test_function([[3, 4], [4, 3]]) # input array with two elements

## More test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[4, 0, 6, 2, 5, 9, 8], [9640, 852]])


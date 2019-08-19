## Search in a Rotated Sorted Array

### Problem statement
> You are given a sorted array which is rotated at some random pivot point. <br />
>
> Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]. <br /> 
>
> You are given a target value to search. If found in the array return its index, otherwise return -1. <br />
> You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`. <br />
>
> Example: <br />
>
> Input: `nums = [4,5,6,7,0,1,2], target = 0, Output: 4`

### Solution
- [rotated_array_search.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/Rotated_Array_Search.py)

### Code Design

- The code recursively search for number using Binary Search Algorithm. 
- Since the input is a rotated array, it's not straightforward to choose left/right part of an array
- The key logic is to find either left half side or right half side of an array where a number potentially can lie. 
- There could be two polssible scenarios, if the number lies in left half of a rotated array.
  1. When pivot point is after mid-array element - Number is greater than first element and less than mid-array element
  2. When the pivot point is before mid-array element - Number is greater than first element, greater than mid-array element and greater than last element.
- If the number is not in left-half, following condition ensures that it's in right half. 
  1. If number is less than the last element of an array.
- If both of above conditions are not valid, the array does not contains the number, hence it should return -1. 

### Efficiency

#### Time Complexity
- The code uses a modified version of Binary Search Algorithm and hence divides problem size into half after each recursion. Therefore, time complexity is `O(log(n))`

#### Space Complexity
- The helper function recursively passes local array for each recursion. However code does execute in parallel. Hence, if input size is n, space is always < 3n. complexity for helper function is `O(n)`.
- Thus overall space complexity is input array space + stack-array space during recursion, which is `O(n) + O(n)`. i.e `O(n)`.  

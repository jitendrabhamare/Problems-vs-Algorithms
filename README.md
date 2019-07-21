# Finding the Square Root of an Integer

### Problem statement

> Find the square root of the integer without using any Python library. You have to find the floor value of the square root.<br />
> For example if the given number is 16, then the answer would be 4.<br />
> If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.<br />
> The expected time complexity is `O(log(n))`<br />

### Code Design

- The code does not use any external library.
- The function 'sqrt' calls a recursive helper function - 'sqrt\_helper' that returns square-root of a number using binary-search algorithm


### Efficiency

- The code uses binary search algorithm and hence divides problem size into half after each recursion. Therefore, time complexity is `O(log(n))`

### Solution

- [find_sqrt.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/find_sqrt.py)


# Search in a Rotated Sorted Array

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
- The code uses a modified version of Binary Search Algorithm and hence divides problem size into half after each recursion. Therefore, time complexity is `O(log(n))`

### Solution
- [rotated_array_search.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/rotated_array_search.py)

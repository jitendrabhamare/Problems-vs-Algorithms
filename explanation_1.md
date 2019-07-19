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



# Search in a Rotated Sorted Array

### Problem statement
> You are given a sorted array which is rotated at some random pivot point. <br />

> Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]. <br /> 

> You are given a target value to search. If found in the array return its index, otherwise return -1. <br />
> You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of `O(log n)`. <br />

> Example: <br />

> Input: `nums = [4,5,6,7,0,1,2], target = 0, Output: 4`

### Code Design
### Efficiency

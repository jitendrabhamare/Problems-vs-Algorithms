## Rearrange Array Elements

### Problem statement
> Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
>
> for e.g. [1, 2, 3, 4, 5]
>
>The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.


### Solution
- [rearrange_digits.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/Rearrange_Digits.py)

### Code Design

-   Two step process:
    1. Sort an array using Merge Sort
    2. Create two arrays such that sum of joined number is max
        - Create two empty array and pop largest number from an sorted_list.
        - And push into each empty array one by one
        - This also ensures that the number of digits in both the numbers cannot differ by more than 1
        - Convert two arrays into numbers and create and return output_list

### Efficiency

#### Time Complexity
- Merge Sort takes `O(nlog(n))` time. 
- To create two num\_list, it runs while loops once (passes though all elements of an array once), hence it takes `O(n)` time.
- Two `join` sub-arrays into numbers, it runs for loop (two times each) which takes 2 x n/2 time. Hence `O(n)`
- Thus overall time complexity is `O(nlog(n))`

#### Space Complexity
- Space complexity for Merge-Sort is `O(n)`.
- Subarrays take size of `2 x O(n/2).` which is `O(n)`. 
- Overall Space complexity is `O(n)`



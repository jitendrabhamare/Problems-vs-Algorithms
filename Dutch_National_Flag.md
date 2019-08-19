## Dutch National Flag Problem


### Problem statement
> Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
>
> Note: `O(n)` does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.

### Solution
- [sort_012.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/Sort_012.py)

### Design Logic
- The idea is to put 0 and 2 in their correct positions, which will make sure all the 1s are automatically placed in their right positions
- Two pointers (for 0 and 2) are used that start from start and end of the list. Front index iterate once through the list and accordingly exchange values with 0 and 2 pointer index. 

### Efficiency

#### Time Complexity
- As front\_index in while loop traverses through the list only once, time complexity is `O(n)`.

#### Space Complexity
- As input array size is n, space complexity is `O(n)`.


## Max and Min in an Unsorted Array

### Problem Statement
> In this problem, we will look for smallest and largest integer from a list of unsorted integers. <br />
> The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max. <br />
> Is it possible to find the max and min in a single traversal?

### Solution
- [get_min_max.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/Get_Min_Max.py)

### Design Logic
- Assign first number of an array to both min and max
- Traverse once through an array compare each element with min and max num.
- Reassign min, max based on comparison

### Efficiency

#### Time Complexity
- The code traverse through the list just once.
- Hence time complexity is `O(n)`.

#### Space Complexity
- If input size is n, space complexity is `O(n)`


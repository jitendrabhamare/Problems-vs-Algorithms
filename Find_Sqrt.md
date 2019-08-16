# Finding the Square Root of an Integer

### Problem statement

> Aim is to find a square root of an integer **without using any Python library**. The answer should be the floor value of the square root.<br />
> **For example** if the given number is 16, then the answer would be 4.<br />
> If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.<br />
> The expected time complexity is **`O(log(n))`**<br />

### Solution

- [find_sqrt.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/find_sqrt.py)

### Code Design

- The code does not use any external library.
- The function 'sqrt' calls a recursive helper function - 'sqrt\_helper' that returns square-root of a number using **binary-search algorithm**


### Efficiency

#### Time Complexity
- The code uses binary search algorithm and hence divides problem size into half after each recursion. Therefore, time complexity is **`O(log(n))`**

#### Space Complexity
- The code does not create any extra array. 
- Size of input array is n, hence space complexity **`O(n)`**

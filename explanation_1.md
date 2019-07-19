# Finding the Square Root of an Integer

### Problem statement

> Find the square root of the integer without using any Python library. You have to find the floor value of the square root.
> For example if the given number is 16, then the answer would be 4.
> If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.
> The expected time complexity is `O(log(n))`

### Code Design

- The code does not use any external library.
- The function 'sqrt' calls a recursive helper function - 'sqrt\_helper' that returns square-root of a number using binary-search algorithm


### Efficiency

- The code uses binary search algorithm and hence divides problem size into half after each recursion. Therefore, time complexity is `O(log(n))`

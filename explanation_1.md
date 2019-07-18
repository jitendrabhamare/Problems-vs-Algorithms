# Finding the Square Root of an Integer

### Code Design

- The code does not use any external library.
- The function 'sqrt' calls a recursive helper function - 'sqrt\_helper' that returns square-root of a number using binary-search algorithm


### Efficiency

- The code uses binary search algorithm and hence divides problem size into half after each recursion. Therefore, time complexity is `O(log(n))`

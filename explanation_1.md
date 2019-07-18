# Finding the Square Root of an Integer

### Code Design

- The code does not use any external library.
- The function 'sqrt' calls a recursive helper function - 'sqrt\_helper' that returns square-rootof a number using binary-search algorithm


### Efficiency

- the code uses binary search algorithm and hence divides problem size into half after each recursion. therefore, time complexity is `O(logn)`

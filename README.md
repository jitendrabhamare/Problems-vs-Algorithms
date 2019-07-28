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

#### Time Complexity
- The code uses binary search algorithm and hence divides problem size into half after each recursion. Therefore, time complexity is `O(log(n))`

#### Space Complexity
- The code does not create any extra array. 
- Size of input array is n, hence space complexity `O(n)`


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

#### Time Complexity
- The code uses a modified version of Binary Search Algorithm and hence divides problem size into half after each recursion. Therefore, time complexity is `O(log(n))`

#### Space Complexity
- The helper function recursively passes local array for each recursion. However code does execute in parallel. Hence, if input size is n, space is always < 3n. complexity for helper function is `O(n)`.
- Thus overall space complexity is input array space + stack-array space during recursion, which is `O(n) + O(n)`. i.e `O(n)`.  



### Solution
- [rotated_array_search.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/rotated_array_search.py)


# Rearrange Array Elements

### Problem statement
> Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. You can assume that all array elements are in the range [0, 9]. The number of digits in both the numbers cannot differ by more than 1. You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).
>
> for e.g. [1, 2, 3, 4, 5]
>
>The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

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


### Solution
- [rearrange_digits.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/rearrange_digits.py)



# Dutch National Flag Problem


### Problem statement
> Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. You're not allowed to use any sorting function that Python provides.
>
> Note: `O(n)` does not necessarily mean single-traversal. For e.g. if you traverse the array twice, that would still be an `O(n)` solution but it will not count as single traversal.


### Design Logic
- The idea is to put 0 and 2 in their correct positions, which will make sure all the 1s are automatically placed in their right positions
- Two pointers (for 0 and 2) are used that start from start and end of the list. Front index iterate once through the list and accordingly exchange values with 0 and 2 pointer index. 

### Efficiency

#### Time Complexity
- As front\_index in while loop traverses through the list only once, time complexity is `O(n)`.

#### Space Complexity
- As input array size is n, space complexity is `O(n)`.

### Solution
- [sort_012.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/sort_012.py)


# Autocomplete with Tries

### Problem Statement
> A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
>
> Implement a code that will return all complete word suffixes that exist in the trie. 
>
> For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from node. 


### Design Logic

### Efficiency

#### Time Complexity

#### Space Complexity

### Solution




# Max and Min in an Unsorted Array

### Problem Statement
> In this problem, we will look for smallest and largest integer from a list of unsorted integers. <br />
> The code should run in O(n) time. Do not use Python's inbuilt functions to find min and max. <br />
> Is it possible to find the max and min in a single traversal?

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

### Solution
- [get_min_max.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/get_min_max.py)



# HTTPRouter using a Trie 

### Problem Statement
> Implement an HTTPRouter like you would find in a typical web server using the Trie data structure. <br />
> There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.
> 
> The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.
> 
> Trie will contain a part of the http path at each node, building from the root node `/`.
> 
> We could split the path into letters similar to how we did the autocomplete Trie, but this would result in a Trie with a very large number of nodes and lengthy traversals if we have a lot of pages on our site. A more sensible way to split things would be on the parts of the path that are separated by slashes ("/"). A Trie with a single path entry of: "/about/me" would look like:
> 
> `(root, None) -> ("about", None) -> ("me", "About Me handler")`
> 
> The router will initialize itself with a RouteTrie for holding routes and associated handlers. It should also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.
>
> Hint: the RouteTrie stores handlers under path parts, so remember to split your path around the '/' character
> 
> Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.
> 
> More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.



### Design Logic/Features
- Three Class data types are used namely Router, RouteTrie and RouteTrieNode.
- Router.add\_handler is used to add a new handler with the help of RouteTrie.insert and RouteTrieNode.insert.
- Router.lookup is used to find a handler with the help of RouteTrie.find.
- Added a "not found handler" to the Router which is returned whenever a path is not found in the Trie.
- Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

### Efficiency

#### Time Complexity
- Run time of both 'add_handler' and 'lookup' logic is based on depth of the Trie.
- For depth n, time complexity is `O(n)`.

#### Space Complexity
- The size of data-structure increases linearly. Therefore, if input size is n, space complexity is `O(n)`

### Solution
- [HTTPRouter.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/HTTPRouter.py)

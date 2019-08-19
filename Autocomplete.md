## Autocomplete with Tries

### Problem Statement
> A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
>
> Implement a code that will return all complete word suffixes that exist in the trie. 
>
> For example, if our Trie contains the words `["fun", "function", "factory"]` and we ask for suffixes from the `f` node, we would expect to receive `["un", "unction", "actory"]` back from node. 

### Solution
- [autocomplete.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/Autocomplete.py)

### Design Logic
- A function `suffix` on the TrieNode object is implemented that returns all complete word suffixes that exist below it in the trie.
- It takes care of corner cases including empty nodes. Recursively calls itself (based on DFS algorithm) and form string from children keys.

### Efficiency

#### Time Complexity
- Both 'insert' and 'find' functions involve one for loop each, and time complexity for these operations is `O(n)`.
- The 'suffixes' function contains a for loop with recursion, hence time complexity is a product of recursion depth and trie depth. Hence it's `O(n^2)`

#### Space Complexity
- The size of data-structure increases linearly. Therefore, if input size is n, space complexity is `O(n)`

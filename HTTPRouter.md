## HTTPRouter using a Trie 

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

### Solution
- [HTTPRouter.py](https://github.com/jitendrabhamare/Problems-vs-Algorithms/blob/master/HTTPRouter.py)

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


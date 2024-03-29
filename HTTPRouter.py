# HTTPRouter using a Trie
# Author: Jitendra Bhamare

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=''):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        #self.is_leaf = False
        self.handler = handler

    def insert(self, page, handler=''):
        # Insert the node as before
        if page not in self.children:
            self.children[page] = RouteTrieNode(handler)


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=''):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path_list, handler='', default_handler=''):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root

        for page in path_list:
            if page not in current_node.children:
                current_node.insert(page, default_handler)
            current_node = current_node.children[page]

        current_node.handler = handler


    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        router = Router()

        for page in path_list:
            if page not in current_node.children:
                return router.default_handler
            current_node = current_node.children[page]
        
        return current_node.handler


# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler='root handler', default_handler='not found handler'):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.rootRouteTrie = RouteTrie(handler)
        self.default_handler = default_handler

    def add_handler(self, path, handler='not found handler'):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.rootRouteTrie.insert(path_list, handler, self.default_handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        #print(path_list)
        if path_list == []:
            return self.rootRouteTrie.root.handler
        return self.rootRouteTrie.find(path_list)


    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_list = path.split('/')
        path_list = ' '.join(path_list).split()
        return path_list


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print("\n")
print("-------------------------------------------")
print("Test case 1")
print("-------------------------------------------")
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one        

## New Test case
router1 = Router("This is a root handler", "no handler is available") # remove the 'not found handler' if you did not implement this
router1.add_handler("/home/about/subjects/", "subjects handler")  # add a route
router1.add_handler("/home/about/subjects/history", "history handler")  # add a route
router1.add_handler("/home/about/subjects/maths", "maths handler")  # add a route
router1.add_handler("/home/about/subjects/computers")  # add a route

# some lookups with the expected output
print("\n")
print("-------------------------------------------")
print("Test case 2")
print("-------------------------------------------")
print(router1.lookup("/")) # should print 'this is a root handler'
print(router1.lookup("")) # should print 'this is a root handler'
print(router1.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router1.lookup("/home/about/")) # should print 'no handler is available
print(router1.lookup("/home/about/subjects")) # should print 'subjects handler'
print(router1.lookup("/home/about/subjects/history/")) # should print 'history handler'
print(router1.lookup("/home/about/subjects/maths/")) # should print 'maths handler'
print(router1.lookup("/home/about/subjects/computers/")) # should print 'no handler is available'

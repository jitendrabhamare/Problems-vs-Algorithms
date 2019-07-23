## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.word_finished = False
        self.children = {}
        
    
    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()
        
## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
            
        current_node.word_finished = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        
        return current_node.word_finished
        #return current_node


word_list = ['apple', 'bear', 'goo', 'good', 'goodbye', 'goods', 'goodwill', 'gooses'  ,'zebra']
word_trie = Trie()

## Add words
for word in word_list:
    word_trie.insert(word)

print(word_trie)

# Test words
test_words = ['bear', 'goo', 'good', 'goos']
for word in test_words:
    #print(word_trie.find(word).children)
    if word_trie.find(word):
        print('"{}" is a word.'.format(word))
    else:
        print('"{}" is not a word.'.format(word))


    

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # O(m) - where m is the length of the word
    def insert(self, word: str ):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.isEndOfWord = True

    # O(m) - where m is the length of the word
    def search(self, word: str):
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.isEndOfWord

    # O(m) - where m is the length of the prefix
    def has_prefix(self, prefix: str):
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return True
    
    # O(m) - where m is the length of the word
    def delete(self, word: str):
        return self._delete(self.root, word, 0)

    # O(m + k) - where m is the length of the prefix and k is the total number of characters in all suffix
    def starts_with(self, prefix: str):
        words = []
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return words
            
            curr = curr.children[char]
        
        def _dfs(curr, path):
            if curr.isEndOfWord:
                words.append(''.join(path))

            for char, child_node in curr.children.items():
                _dfs(child_node, path + [char])
        
        _dfs(curr, list(prefix))

        return words
    
    # O(n) - where n is the number of nodes in the Trie
    def list_words(self):
        words = list()

        def _dfs(curr, path):
            if curr.isEndOfWord:
                words.append(''.join(path))

            for char, child_node in curr.children.items():
                _dfs(child_node, path + [char])
        
        _dfs(self.root, [])

        return words
    
    # 
    #   Example: Delete The Word "mini" from the Trie.
    
    ##  Example Trie : mini, minimal, minimum, minimalism

    ##  Recursive through the _delete method till we hit the end where index = 4
    ##  we will find that the 'i' at the end of 'mini' still flag with isEndOfWord
    ##  so we change that. Even if it can loop through the search method, it will 
    ##  still not find the word since isEndOfWord is now False.

    def _delete(self, curr, word, index):
        if index == len(word): 
            if not curr.isEndOfWord:
                return False
            
            curr.isEndOfWord = False # remove the flag 'isEndOfWord'

            return len(curr.children) == 0
        
        char = word[index] 
        node = curr.children.get(char)

        if node is None:
            return False
        
        del_curr = self._delete(node, word, index + 1)

        if del_curr:
            del curr.children[char]
            return len(curr.children) == 0 and not curr.isEndOfWord
        
        return False
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str ):
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.isEndOfWord = True

    def search(self, word: str):
        curr = self.root

        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return curr.isEndOfWord

    def has_prefix(self, prefix: str):
        curr = self.root

        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
            
        return True
    
    def delete(self, word: str):
        return self._delete(self.root, word, 0)

    def starts_with(self, prefix: str):
        pass
    
    def list_words(self):
        pass
    
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
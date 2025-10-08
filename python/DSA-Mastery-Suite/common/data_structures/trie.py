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

    def _delete(self, curr, word, index):
        if index == len(word):
            if not curr.isEndOfWord:
                return False
            
            curr.isEndOfWord = False

            return len(curr.children) == 

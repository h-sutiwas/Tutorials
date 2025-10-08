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

    def delete(self, word: str):
        pass

    def has_prefix(self, prefix: str):
        pass

    def starts_with(self, prefix: str):
        pass
    
    def list_words(self):
        pass
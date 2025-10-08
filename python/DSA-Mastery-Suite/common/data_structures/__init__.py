from trie import Trie, TrieNode

trie = Trie()
trie.insert("hello")
trie.insert("hell")
trie.insert("helicopter")

print(trie.search("hell"))
print(trie.search("hel"))
print(trie.search("help"))
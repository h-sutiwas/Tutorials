from trie import Trie, TrieNode

trie = Trie()

trie.insert("hello")
trie.insert("hell")
trie.insert("helicopter")
trie.insert("henry")
trie.insert("min")
trie.insert("mini")
trie.insert("minimal")
trie.insert("minimum")

print(trie.search("hell"))
print(trie.search("hel"))
print(trie.search("help"))

print(trie.list_words())

print(trie.has_prefix("mi"))

print(trie.starts_with("mi"))

trie.delete('min')
trie.delete('minimal')

print(trie.starts_with("mi"))
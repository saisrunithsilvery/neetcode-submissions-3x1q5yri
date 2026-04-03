class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:          # fixed spelling
                node = node.children[char]     # fixed spelling
            else:
                node.children[char] = TrieNode()  # fixed spelling
                node = node.children[char]         # fixed spelling
        node.is_end = True            

    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i not in node.children:    # fixed spelling + removed ()
                return False
            node = node.children[i]       # fixed spelling
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:  # removed ()
                return False
            node = node.children[char]
        return True
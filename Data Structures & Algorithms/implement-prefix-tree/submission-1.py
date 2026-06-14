class Node():
    def __init__(self):
        self.children = {}
        self.isend = False    

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                newNode =  Node()
                node.children[char] = newNode

                node = node.children[char]
        node.isend = True          


    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children :
                node = node.children[char]
            else:
                return False
        return node.isend            


        

    def startsWith(self, prefix: str) -> bool:

        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return True            
        
        
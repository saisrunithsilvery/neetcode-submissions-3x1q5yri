from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isend = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build Trie from words
        self.root = TrieNode()
        for word in words:
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()  # Direct assignment, not append
                node = node.children[char]
            node.isend = True

        rows, cols = len(board), len(board[0])
        result = []
        visited = set()

        def dfs(r, c, node, word):
            # Boundary check, visited check, character check
            if r < 0 or r == rows or c < 0 or c == cols:
                return
            if (r, c) in visited:
                return
            
            char = board[r][c]
            if char not in node.children:
                return

            # Move deeper into Trie
            node = node.children[char]
            word = word + char
            visited.add((r, c))

            # Found a word
            if node.isend:
                result.append(word)
                node.isend = False  # Prevent duplicates (optional, or use set)

            # Explore 4 directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtrack
            visited.remove((r, c))

        # Start DFS from each cell
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, self.root, "")

        return result



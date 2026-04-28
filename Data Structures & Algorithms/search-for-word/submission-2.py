class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def bt(i, j, k):
            # Base: all characters matched
            if k == len(word):
                return True

            # Boundary check + character match
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[k]:
                return False

            # Mark as visited by replacing with '#'
            temp = board[i][j]
            board[i][j] = '#'

            # Explore all 4 directions
            found = (bt(i + 1, j, k + 1) or
                     bt(i - 1, j, k + 1) or
                     bt(i, j + 1, k + 1) or
                     bt(i, j - 1, k + 1))

            # Restore the cell (backtrack)
            board[i][j] = temp

            return found

        for i in range(rows):
            for j in range(cols):
                if bt(i, j, 0):
                    return True

        return False
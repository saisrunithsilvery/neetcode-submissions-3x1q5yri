class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def bt(i, j, k):

            # all characters matched
            if k == len(word):
                return True

            temp = board[i][j]
            board[i][j] = "#"

            directions = [
                (1, 0),
                (-1, 0),
                (0, 1),
                (0, -1)
            ]

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if (
                    0 <= ni < rows and
                    0 <= nj < cols and
                    board[ni][nj] == word[k]
                ):
                    if bt(ni, nj, k + 1):
                        board[i][j] = temp
                        return True

            board[i][j] = temp
            return False

        for i in range(rows):
            for j in range(cols):

                # word[0] already matched here
                if board[i][j] == word[0]:

                    # now search for word[1]
                    if bt(i, j, 1):
                        return True

        return False
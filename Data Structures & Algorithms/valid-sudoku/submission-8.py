from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for j in range(9):
                if board[r][j] ==".":
                    continue
                if board[r][j] in rows[r] or board[r][j] in columns[j] or board[r][j] in square[(r//3,j//3)]:
                    return False

                rows[r].add(board[r][j])
                columns[j].add(board[r][j])
                square[(r//3,j//3)].add(board[r][j])

        return True            


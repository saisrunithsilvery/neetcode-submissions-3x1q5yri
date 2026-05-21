class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        sub = defaultdict(set)


        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == '.':
                    continue

                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in sub[(i//3, j//3)]:
                    return False

                else:

                    rows[i].add(board[i][j])    
                    cols[j].add(board[i][j])
                    sub[(i//3, j//3)].add(board[i][j])
        return True            

        
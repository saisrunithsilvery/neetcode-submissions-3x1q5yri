class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(0,len(board)):
            val1 = set()
            val2=set()
            for j in range(0, len(board)):

                    
                if board[i][j] != '.':
                    if board[i][j] in val1:
                        return False 
                    val1.add(board[i][j])

                if board[j][i]!='.':
                    if board[j][i] in val2:
                        return False        
                    val2.add(board[j][i])

        for i in range(0,9,3):
            for j in range(0,9,3):
                val = set()

                for i1 in range(i, i+3):
                    for j1 in range(j, j+3):
                        if board[i1][j1]!='.':

                            if board[i1][j1] in val:
                                return False

                            val.add(board[i1][j1])

        return True                                 





        
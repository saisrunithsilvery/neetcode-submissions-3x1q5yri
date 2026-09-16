class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)


        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == ".":
                    continue

                if board[row][col] not in rows[row] :
                    rows[row].add(board[row][col])
                else:
                    return False

                if board[row][col] not in columns[col] :
                    columns[col].add(board[row][col])
                else:
                    return False    

                if board[row][col] not in boxes[tuple([row//3, col//3])]:
                    boxes[tuple([row//3, col//3])].add(board[row][col])

                else:
                    return False   
        return True             



        
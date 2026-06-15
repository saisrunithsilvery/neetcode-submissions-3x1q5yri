class Solution:
    def solve(self, board):
        if not board:
            return
        rows, cols = len(board), len(board[0])
        safe = set()
        def dfs(r, c):
            if (r < 0 or r >= rows or c < 0 or c >= cols
                    or (r, c) in safe
                    or board[r][c] == 'X'):
                return
            safe.add((r, c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                dfs(r + dr, c + dc)
        # Step 1 & 2: DFS from all border O's
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows-1 or c == 0 or c == cols-1):
                    if board[r][c] == 'O':
                        dfs(r, c)
        # Step 3: Flip all non-safe O's to X
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and (r, c) not in safe:
                    board[r][c] = 'X'

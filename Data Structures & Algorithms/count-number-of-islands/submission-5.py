class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        self.visit = set()
        count = 0
        
        def dfs(row, col):
            if row == rows or col == cols or (row,col) in self.visit or row < 0 or col < 0 or grid[row][col] == "0":
                return

            self.visit.add((row, col))

            directions = [(0,1), (1,0), (0, -1), (-1, 0)]

            for r, c in directions:
                dfs(row+r, col+c)

        # BUG FIXES BELOW:
        for i in range(rows):           # ❌ Was: for i in rows:
            for j in range(cols):       # ❌ Was: for j in cols:
                if (i, j) not in self.visit and grid[i][j] == "1":  # ❌ Was: not in visit
                    dfs(i, j)
                    count += 1

        return count
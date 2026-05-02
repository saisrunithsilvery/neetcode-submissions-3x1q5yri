class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        memo = [[-1]*n for _ in range(0,m)]

        def solve(x, y):
        
            if x == m-1 and y == n-1:
                return 1
            
            # out of bounds → invalid path
            if x >= m or y >= n:
                return 0

            if memo[x][y] != -1:
                return memo[x][y]
            memo[x][y] = solve(x+1, y) + solve(x, y+1)
            return memo[x][y]

        return solve(0, 0)
        
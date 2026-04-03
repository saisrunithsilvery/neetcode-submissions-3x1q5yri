class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0]*n for _ in range(0, m)]

        def solve(i, j):

            if i>= m or j >= n :
                return 0

            if i == m-1 and j== n-1:
                return 1

            if dp[i][j] != 0:
                return dp[i][j]    

            dp[i][j] = solve(i+1, j) + solve(i, j+1)
            return dp[i][j]

        return solve(0,0)

        




        
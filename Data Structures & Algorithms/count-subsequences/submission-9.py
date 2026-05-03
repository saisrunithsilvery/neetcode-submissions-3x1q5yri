
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        
        dp = [[0]*(m+1) for _ in range(0,n+1)]

        def solve(i, j):

             

            if j == m:
                return 1
            
            if i == n :
                return 0   

            if dp[i][j] != 0:
                return dp[i][j]
            x = 0
            y = 0
            if s[i]== t[j]:
                x = solve(i+1, j+1)
            y = solve(i+1, j)

            dp[i][j] = x + y

            return dp[i][j]

        return solve(0,0)            

                    
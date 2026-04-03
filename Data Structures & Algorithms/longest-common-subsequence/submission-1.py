class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        n = len(text1)
        m = len(text2)
        dp = [[0]*m for _ in range(0,n)]

        def solve(x, y):

        

            if x >= n or y >=m:
                return 0

            if dp[x][y] != 0:
                return dp[x][y]    

            if text1[x] == text2[y]:

                dp[x][y] = 1+solve(x+1, y+1)   
                return dp[x][y] 

            else:
                dp[x][y] = max(solve(x+1, y), solve(x, y+1))  
                return dp[x][y] 

        return solve(0,0)             


        
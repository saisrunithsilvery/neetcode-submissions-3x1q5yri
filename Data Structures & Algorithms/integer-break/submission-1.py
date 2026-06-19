class Solution:
    def integerBreak(self, n: int) -> int:
       
        dp = [0] * (n + 1)
        
        # Base case
        dp[1] = 1  # Can't break 1, but set for safety
        dp[2] = 1  # Only option: 1+1, product = 1
        
        for i in range(3, n + 1):
            for j in range(1, i):
                # Compare:
                # - Keep (i-j) as-is: j * (i-j)
                # - Break (i-j) further: j * dp[i-j]
                dp[i] = max(dp[i], j * dp[i - j])
        
        return dp[n]


    
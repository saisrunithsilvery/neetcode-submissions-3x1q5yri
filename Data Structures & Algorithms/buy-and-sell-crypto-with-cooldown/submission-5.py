class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        
        # instead of dp[i], dp[i+1], dp[i+2]
        # just keep:
        next1 = [0, 0]   # represents dp[i+1]
        next2 = [0, 0]   # represents dp[i+2]
        
        for i in range(n-1, -1, -1):
            curr = [0, 0]
            curr[0] = max(-prices[i] + next1[1], next1[0])
            curr[1] = max(prices[i] + next2[0], next1[1])
            
            # slide the window forward
            next2 = next1
            next1 = curr
        
        return curr[0]

            
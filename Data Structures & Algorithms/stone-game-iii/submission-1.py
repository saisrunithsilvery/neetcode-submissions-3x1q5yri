class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0  # No stones left, advantage = 0
        
        for i in range(n - 1, -1, -1):
            for k in range(1, 4):
                if i + k <= n:
                    current_take = sum(stoneValue[i:i+k])
                    alice_advantage = current_take - dp[i+k]
                    dp[i] = max(dp[i], alice_advantage)
        
        diff = dp[0]
        if diff > 0:
            return "Alice"
        elif diff < 0:
            return "Bob"
        else:
            return "Tie"



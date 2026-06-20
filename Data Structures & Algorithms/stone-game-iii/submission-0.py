class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        # dp[i] = max advantage (Alice - Bob) from stones[i:] onward
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0  # No stones left, advantage = 0
        
        for i in range(n - 1, -1, -1):
            # Try taking 1, 2, or 3 stones
            for k in range(1, 4):
                if i + k <= n:
                    # Alice takes k stones
                    # Her advantage: stones she took - (best opponent can do next)
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



class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        INF = float('inf')

        dp = [[INF] * (amount + 1) for _ in range(n + 1)]

        # base case: total == amount → 0 coins needed (for every i, including n)
        for i in range(n + 1):
            dp[i][amount] = 0

        for i in range(n - 1, -1, -1):
            for t in range(amount - 1, -1, -1):
                take = INF
                if t + coins[i] <= amount:          # total > amount → inf
                    take = 1 + dp[i][t + coins[i]]
                skip = dp[i + 1][t]
                dp[i][t] = min(take, skip)

        return dp[0][0] if dp[0][0] != INF else -1
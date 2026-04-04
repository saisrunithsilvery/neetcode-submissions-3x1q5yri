class Solution:
    def change(self, amount: int, coins) :
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 1
        for idx in range(n - 1, -1, -1):
            for amnt in range(1, amount + 1):
                dp[idx][amnt] = dp[idx + 1][amnt]
                if amnt >= coins[idx]:
                    dp[idx][amnt] += dp[idx][amnt - coins[idx]]
        return dp[0][amount]
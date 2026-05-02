class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        nxt = [0] * (amount+1)
        nxt[amount] = 1

        for i in range(n-1, -1, -1):
            curr = [0] * (amount+1)    # ← only here
            curr[amount] = 1
            for amt in range(amount-1, -1, -1):
                curr[amt] = nxt[amt] + (curr[amt+coins[i]] if amt+coins[i] <= amount else 0)
            nxt = curr

        return nxt[0]
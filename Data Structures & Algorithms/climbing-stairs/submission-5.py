class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = [-1] * (n + 1)

        def rec(i):
            if i <= 2:
                return i

            if memo[i] != -1:
                return memo[i]

            memo[i] = rec(i-1) + rec(i-2)
            return memo[i]

        return rec(n)
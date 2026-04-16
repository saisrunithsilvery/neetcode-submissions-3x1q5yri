import sys
sys.setrecursionlimit(10000)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        memo = {}

        def solve(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            if j == m:
                return 1
            if i == n:
                return 0

            if s[i] == t[j]:
                memo[(i, j)] = solve(i+1, j+1) + solve(i+1, j)
            else:
                memo[(i, j)] = solve(i+1, j)

            return memo[(i, j)]

        return solve(0, 0)   # ← fixed: indented inside the method
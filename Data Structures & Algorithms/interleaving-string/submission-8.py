class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case seed — same as: if i == m and j == n: return True
        dp[m][n] = True

        # Fill backwards (since recursion goes i+1, j+1, we iterate in reverse)
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n:
                    continue  # already seeded

                k = i + j  # position in s3

                if i < m and s1[i] == s3[k]:
                    dp[i][j] |= dp[i+1][j]

                if j < n and s2[j] == s3[k]:
                    dp[i][j] |= dp[i][j+1]

        return dp[0][0]
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        count = 0

        # length 1
        for i in range(n):
            dp[i][i] = True
            count += 1

        # length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                count += 1

        # length 3+
        for length in range(3, n+1):
            for j in range(n - length + 1):
                l = j
                r = j + length - 1
                if s[l] == s[r] and dp[l+1][r-1]:
                    dp[l][r] = True
                    count += 1

        return count
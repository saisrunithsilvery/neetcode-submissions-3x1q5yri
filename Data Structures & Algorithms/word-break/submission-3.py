class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordset = set(wordDict)
        n = len(s)

        dp = [False] * (n + 1)
        dp[n] = True  # base case: empty suffix

        for index in range(n - 1, -1, -1):
            for j in range(index + 1, n + 1):
                if s[index:j] in wordset and dp[j]:
                    dp[index] = True
                    break

        return dp[0]
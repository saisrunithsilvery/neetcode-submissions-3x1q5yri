class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * n for _ in range(2)]   # dp[0][i] = max ending at i, dp[1][i] = min ending at i

        dp[0][0] = dp[1][0] = nums[0]
        result = nums[0]

        for i in range(1, n):
            a = dp[0][i - 1] * nums[i]
            b = dp[1][i - 1] * nums[i]
            dp[0][i] = max(nums[i], a, b)
            dp[1][i] = min(nums[i], a, b)
            result = max(result, dp[0][i])

        return result
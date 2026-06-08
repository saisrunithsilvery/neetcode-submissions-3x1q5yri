class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0]*(n+2)

        for i in range(len(nums)-1, -1, -1):
            dp[i] = nums[i]+ dp[i+2]

        return max(dp[0], dp[1])
        
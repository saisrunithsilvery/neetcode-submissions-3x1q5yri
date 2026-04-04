class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
       
        n = len(nums)
        total = sum(nums)
        
        if abs(target) > total:
            return 0
        
        # dp[idx][sum + total] = number of ways to reach sum using first idx nums
        dp = [[0] * (2 * total + 1) for _ in range(n + 1)]
        
        # base case: 0 nums processed, sum=0, 1 way
        dp[0][total] = 1  # offset so sum=0 maps to index total
        
        for idx in range(1, n + 1):
            for s in range(2 * total + 1):
                # add nums[idx-1]
                if s - nums[idx-1] >= 0:
                    dp[idx][s] += dp[idx-1][s - nums[idx-1]]
                # subtract nums[idx-1]
                if s + nums[idx-1] <= 2 * total:
                    dp[idx][s] += dp[idx-1][s + nums[idx-1]]
        
        return dp[n][target + total]
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        x = sum(nums)
        dp = [[-1]*(2*x+1) for _ in range(0,n+1)] 
        def solve(sum1, idx):
            
            if dp[idx][x+sum1]!= -1:
                return dp[idx][x+sum1]
            

            if sum1 == target and idx == n :
                return 1

            if idx >= n :
                return 0    

            dp[idx][x+sum1] = solve(sum1+nums[idx], idx+1) + solve(sum1 - nums[idx], idx+1)
            return dp[idx][sum1+x]

        return solve(0, 0)     

        
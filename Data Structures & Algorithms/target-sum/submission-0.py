class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def solve(sum1, idx):

            

            if sum1 == target and idx == n :
                return 1

            if idx >= n :
                return 0    

            x = solve(sum1+nums[idx], idx+1) + solve(sum1 - nums[idx], idx+1)
            return x

        return solve(0, 0)     

        
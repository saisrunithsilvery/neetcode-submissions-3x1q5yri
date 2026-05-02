class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)
        total = sum(nums)
        memo = {}   # use dictionary — easier for negative keys!

        def solve(i, amt):
            if i == n:
                return 1 if amt == target else 0
            
            if (i, amt) in memo:
                return memo[(i, amt)]
            
            x = solve(i+1, amt + nums[i])
            y = solve(i+1, amt - nums[i])
            
            memo[(i, amt)] = x + y
            return memo[(i, amt)]

        return solve(0, 0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        # memo = [[0]*(n+1) for _ in range(target)]
        n = len(nums)
        def solve(i, amt):

            if i == n:
                return 1 if amt == target else 0
                
            if i > n or amt > target:
                return 0
            

            x = solve( i+1, amt+nums[i])
            y = solve(i+1, amt - nums[i])

            return x+y
        return solve(0, 0)    


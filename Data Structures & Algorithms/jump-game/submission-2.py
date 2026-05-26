class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        x = nums[0]

        for i in range(0, len(nums)):

            if i > x:
                return False

            x = max(x, i+nums[i])
        return True        

            



        
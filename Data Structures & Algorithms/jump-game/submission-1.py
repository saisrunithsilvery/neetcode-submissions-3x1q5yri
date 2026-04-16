class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        valind = n-1
        for i in range(n-2, -1,-1):

            if i+nums[i]>= valind :
                valind = i

        return valind == 0           

        
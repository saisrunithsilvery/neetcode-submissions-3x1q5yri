class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum1 = 0
        result = -float('inf')
        for i in range(0, n):

            sum1 = sum1 + nums[i]
            result = max(result, sum1)

            if sum1 < 0:
                sum1 = 0
        return result        

           
        
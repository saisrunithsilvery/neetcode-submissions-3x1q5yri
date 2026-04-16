class Solution:
    def jump(self, nums: List[int]) -> int:

        val = nums[0]
        max1 = 0
        result = 1
        n = len(nums)

        if n <= 1:
            return 0
        for i in range(1, n):

            if i > val :
                val = max1
                result += 1

            max1 = max(max1, i+nums[i])    

        return result        






            







        
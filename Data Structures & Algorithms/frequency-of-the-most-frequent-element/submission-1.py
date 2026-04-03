class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        sum1=0
        left =0
        res =0
        for right in range(0,len(nums)):
            sum1 +=nums[right]
            
            while nums[right]*(right-left +1) - sum1 >k:
                sum1 -=nums[left]
                left +=1

            res =max(right -left +1, res)
        return res
            

        
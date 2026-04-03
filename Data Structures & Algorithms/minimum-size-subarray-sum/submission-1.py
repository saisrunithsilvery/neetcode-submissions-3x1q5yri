class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left =0
        sum =0
        res = float('inf')
        for right in range(0,len(nums)):
            
            sum +=nums[right]
            while sum >=target:
                res = min(right -left +1, res)
                sum -=nums[left]
                left +=1
                
                
        return res if res !=float('inf') else 0
                
                
        
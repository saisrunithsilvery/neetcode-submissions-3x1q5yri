class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count={}
        for i in range(0,len(nums)):
            remaining = target - nums[i]
        
            if remaining in count:
                return [count[remaining],i] 
            count[nums[i]] = i    

                




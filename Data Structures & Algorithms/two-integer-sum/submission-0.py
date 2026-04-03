class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x={}
        for i in range(len(nums)):
            
            cmp= target - nums[i]

            if cmp in x:
                return [x[cmp], i]

            x[nums[i]] = i
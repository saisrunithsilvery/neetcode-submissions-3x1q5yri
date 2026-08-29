class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashset = {}

        for i, val in enumerate(nums):

            remaining = target - val
            if remaining in hashset:
                return [hashset[remaining], i]
            hashset[val] = i 
               


        
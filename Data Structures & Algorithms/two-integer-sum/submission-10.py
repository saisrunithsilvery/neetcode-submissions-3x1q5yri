class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashset = {}

        for i, num in enumerate(nums):
            remaining = target - num

            if remaining in hashset:
                return list([hashset[remaining], i ])

            hashset[num] = i    




        

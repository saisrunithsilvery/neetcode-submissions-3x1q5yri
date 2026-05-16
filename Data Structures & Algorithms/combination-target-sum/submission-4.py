from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def backtrack(i, path, remaining):  # Add index parameter
            if remaining == 0:
                res.append(path[:])
                return
            
            for j in range(i, len(nums)):  # Start from i, not 0
                if nums[j] > remaining:
                    break
                backtrack(j, path + [nums[j]], remaining - nums[j])  # Pass j, not index

        backtrack(0, [], target)
        return res
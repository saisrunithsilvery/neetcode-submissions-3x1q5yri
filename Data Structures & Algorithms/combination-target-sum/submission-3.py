from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return

            if i >= len(nums) or total > target:
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i, total + nums[i])   # stay at i because reuse allowed
            subset.pop()

            # exclude nums[i]
            dfs(i + 1, total)         # move to next number

        dfs(0, 0)
        return res
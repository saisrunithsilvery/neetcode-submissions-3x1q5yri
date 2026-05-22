class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []
        
        def backtrack(i, current_sum):
            # Base case: exceeded target
            if current_sum > target:
                return
            
            # Base case: found valid combination
            if current_sum == target:
                res.append(subset.copy())
                return
            
            # Base case: no more elements to consider
            if i >= len(nums):
                return
            
            # Choice 1: Include nums[i] (can reuse it)
            subset.append(nums[i])
            backtrack(i, current_sum + nums[i])  # Stay at i
            subset.pop()
            
            # Choice 2: Skip nums[i] (move to next)
            backtrack(i + 1, current_sum)
        
        backtrack(0, 0)  # Call BEFORE return!
        return res
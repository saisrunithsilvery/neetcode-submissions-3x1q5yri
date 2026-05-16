class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            if remaining < 0:
                return
            
            # Try each number from 'start' onwards
            for i in range(start, len(nums)):
                if nums[i] > remaining:  # Early termination
                    break
                
                # Include nums[i] and allow reuse by passing 'i' (not 'i+1')
                backtrack(i, path + [nums[i]], remaining - nums[i])
        
        backtrack(0, [], target)
        return res
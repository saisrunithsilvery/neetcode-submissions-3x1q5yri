class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        subset = []
        result = []


        def solve(index):
            nonlocal subset

            if index == len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[index])
            solve(index+1)
            subset.pop()

            solve(index+1)
        solve(0)
        return result    


        
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        subset = []


        def solve(total, index):

            if index == len(nums):
                return 

            if total == target:
                result.append(subset.copy())
                return 

            if total > target:
                return    

            subset.append(nums[index])
            solve(total+nums[index], index)
            subset.pop()

            solve(total, index+1)

        solve(0,0)
        return result    
      







        
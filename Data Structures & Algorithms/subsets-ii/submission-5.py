class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []
        nums.sort()

        def solve(index):

            if index == len(nums):
                result.append(subset.copy())
                return

            #include 

            subset.append(nums[index])
            solve(index+1)
            subset.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            solve(index +1)
        solve(0)    
        return result        
        
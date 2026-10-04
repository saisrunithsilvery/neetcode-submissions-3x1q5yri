class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        
        def solve(index):

            if index == len(nums):
                result.append(nums.copy())
                return

            for i in range(index, len(nums)):

                nums[index], nums[i] = nums[i], nums[index]
                solve(index+1)
                nums[index], nums[i] = nums[i], nums[index]
        solve(0)
        return       result 



        
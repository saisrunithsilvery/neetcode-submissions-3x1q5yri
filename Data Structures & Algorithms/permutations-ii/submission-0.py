class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        result = []
        nums.sort()

        def solve(index):

            if index == len(nums):
                result.append(nums.copy())


            for i in range(index, len(nums)):
                if i < len(nums)-1 and nums[i] == nums[i+1]:
                    continue
                nums[index], nums[i] = nums[i], nums[index]
                solve(index+1) 
                nums[index], nums[i] = nums[i], nums[index]
            return 
        solve(0)
        return result        



        
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset =[]
        res =[]
        i =0
        def dfs(subset, i):

            if i == len(nums):
                res.append(subset[:])
                return

            dfs(subset + [nums[i]], i+1)

            j = i+1
            while j< len(nums) and nums[i] == nums[j]:
                j +=1
            dfs(subset, j)
        dfs(subset, i)
        return res          


        
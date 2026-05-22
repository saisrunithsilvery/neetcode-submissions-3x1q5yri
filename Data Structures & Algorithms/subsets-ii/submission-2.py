class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset =[]
        res =[]
        i =0
        def dfs( i):

            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            j = i+1
            while j< len(nums) and nums[i] == nums[j]:
                j +=1
            dfs(j)
        dfs(i)
        return res          


        
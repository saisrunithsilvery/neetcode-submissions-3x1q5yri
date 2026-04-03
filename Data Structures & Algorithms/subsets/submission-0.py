class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        i=0
        res=[]
        subset =[]
        def dt(subset, i):
            
            if i >= len(nums):        # ✅ use len(nums) instead of 2
                res.append(subset)
                return
            
            dt(subset + [nums[i]], i + 1)
            dt(subset, i + 1)

        dt(subset, i)
        return res        
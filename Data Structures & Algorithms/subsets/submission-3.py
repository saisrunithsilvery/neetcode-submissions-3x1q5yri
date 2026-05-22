class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        i=0
        res=[]
        subset =[]
        def dt(i):
            if i >= len(nums):        
                res.append(subset.copy())
                return
            subset.append(nums[i])    
            dt(i + 1)
            subset.pop()
            dt(i + 1)
        dt( i)
        return res       
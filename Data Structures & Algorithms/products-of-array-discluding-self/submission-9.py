class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        res1=[]
        prefix=1
        for i in nums:
            res1.append(prefix)
            prefix *=i
            
        res2=[1]*len(nums)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res2[i]=postfix
            postfix *=nums[i]
        res=[]    
        for i in range(0, len(nums)):
            res.append(res1[i]*res2[i])

        return res    




        
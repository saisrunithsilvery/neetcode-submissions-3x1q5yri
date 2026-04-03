class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i, a in enumerate(nums):
            if i>0 and nums[i-1]==a:
                continue

            l=i+1
            r=len(nums)-1
            while l<r:
                if a+nums[l]+nums[r]>0:
                    r -=1
                elif a+nums[l]+nums[r]<0:
                    l +=1
                else:
                    result.append([a,nums[l],nums[r]]) 
                    r -=1
                    l +=1
                    while l<r and nums[l]==nums[l-1]:
                        l +=1

        return result               


        
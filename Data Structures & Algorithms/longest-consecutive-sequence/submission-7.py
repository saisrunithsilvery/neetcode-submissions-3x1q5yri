class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x= set(nums)
        min1 =float('inf')
        max1= float('-inf')
        for i in range(0, len(nums)):
            min1 = min(min1, nums[i])
            max1= max(max1, nums[i])

        count =0
        result =0
        while min1<=max1:
            if min1 in x:
                count +=1
                result = max(count, result)
            else:
                count =0

            min1 +=1    

        return result    
                         
                

        
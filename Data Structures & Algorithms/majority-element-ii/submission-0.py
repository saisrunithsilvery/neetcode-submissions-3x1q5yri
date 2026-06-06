class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x = nums[0]
        y =None
        for i in nums:
            if i!= x:
                y = i
                break

        count1 = 0
        count2 = 0
        for i in range(0, len(nums)):
            if nums[i] == x:
                count1 +=1 
            elif nums[i] == y:
                count2 +=1
            else:
                count1 -=1
                count2 -=1
            if count1 < 0:
                count1 = 1
                x = nums[i]
            if count2 < 0:
                count2 = 1
                y = nums[i]

        result = []
        if count1 > 0 :
            result.append(x)                    
        if count2 > 0 :
            result.append(y)

        return result    

        
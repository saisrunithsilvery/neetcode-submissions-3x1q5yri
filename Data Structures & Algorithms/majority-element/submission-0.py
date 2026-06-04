class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       
        x = nums[0]
        count = 0
        for num in nums:
            if num == x:
                count += 1
            else:
                count -= 1
            if count == 0:
                x = num
                count = 1
        return x
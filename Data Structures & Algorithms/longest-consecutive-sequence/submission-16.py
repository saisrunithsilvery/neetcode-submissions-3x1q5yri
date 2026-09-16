class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        values = set(nums)

        for num in nums:

            if num -1 not in values:
                value = num
                count = 0
                while value in values:
                    count +=1
                    value +=1
                result = max(count, result)

        return result            
                    

        
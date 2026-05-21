class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums :
            return 0

        set1 = set(nums)
        max1 = 1
        for i in range(0, len(nums)):
            if nums[i]-1 in set1:
                continue
            else:
                x = nums[i]
                count = 1
                while True:

                    if x+1 in set1:
                        count +=1
                        x +=1
                    else:
                        break
                max1 = max(max1, count)     

        return max1

                        

        
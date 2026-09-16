class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):

            # skip duplicate nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:

                total = nums[i] + nums[l] + nums[r]

                if total > 0:
                    r -=1

                elif total < 0:
                    l +=1

                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while nums[l] == nums[l+1]:
                        l +=1
                    while nums[r] == nums[r-1]:
                        r -=1    
                    # then move l and r
                    # also think about duplicates
                l +=1
                r -=1    

        return result
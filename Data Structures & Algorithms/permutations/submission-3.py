class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res =[]
        def bt(nums, i):

            if i == len(nums):
                res.append(nums[:])
                return

            j= i
            while j < len(nums):

                nums[i], nums[j] = nums[j], nums[i]
                bt(nums, i+1)
                nums[i],nums[j] = nums[j], nums[i]
                j +=1

        bt(nums, i)   
        return res         





        
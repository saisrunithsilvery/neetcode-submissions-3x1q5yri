class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        i = 0
        res =[]
        def bt(i):

            if i == len(nums):
                res.append(nums[:])
                return

            j = i
            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                bt(i+1)
                nums[i],nums[j] = nums[j], nums[i]
                j +=1

        bt(i)   
        return res         





        
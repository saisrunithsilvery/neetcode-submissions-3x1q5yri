class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        y = len(nums)-1
        for i in range(len(nums)):

            if i > y:
                break

            if nums[i]== 0:
                nums[i], nums[x] = nums[x], nums[i]
                i += 1
            elif nums[i] == 2:
                nums[i], nums[y] = nums[y], nums[i]
                y -=1

        return nums            


        
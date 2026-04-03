class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            tempMax = max(num, curMax * num, curMin * num)
            tempMin = min(num, curMax * num, curMin * num)

            curMax = tempMax
            curMin = tempMin

            res = max(res, curMax)

        return res
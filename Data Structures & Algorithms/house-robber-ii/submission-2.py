class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLine(arr):
            prev2, prev1 = 0, 0
            for num in arr:
                curr = max(prev1, num + prev2)
                prev2 = prev1
                prev1 = curr
            return prev1

        return max(robLine(nums[:-1]), robLine(nums[1:]))
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        mem = [-1] * n

        def memo(i):
            if i < 0:
                return 0

            if mem[i] != -1:
                return mem[i]

            mem[i] = max(memo(i - 1), nums[i] + memo(i - 2))
            return mem[i]

        return memo(n - 1)
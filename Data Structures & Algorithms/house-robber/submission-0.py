class Solution:
    def rob(self, nums: List[int]) -> int:
        n =len(nums)
        mem = [-1]*n

        def memo(n):

            if n <0:
                return 0

            if mem[n]!= -1:
                return mem[n]

            mem[n]= nums[n]+max(memo(n-2), memo(n-3))
            mem[n-1] = nums[n-1]+ max(memo(n-3), memo(n-4))
            return mem[n]
        memo(n-1)
        return max(mem)         
        
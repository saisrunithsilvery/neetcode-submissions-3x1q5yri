class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += n & 1     # check last bit
            n = n >> 1       # shift right
        return res
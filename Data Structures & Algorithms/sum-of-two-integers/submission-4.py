class Solution:
    def getSum(self, a: int, b: int) -> int:


        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry & 0xFFFFFFFF  # ✅ keep within 32 bits
            a = a & 0xFFFFFFFF      # ✅ keep within 32 bits
        return a     
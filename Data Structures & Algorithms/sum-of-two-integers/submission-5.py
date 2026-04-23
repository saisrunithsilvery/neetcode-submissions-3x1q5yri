class Solution:
    def getSum(self, a: int, b: int) -> int:


        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry & 0xFFFFFFFF  # ✅ keep within 32 bits
            a = a & 0xFFFFFFFF 
        if a > 0x7FFFFFFF:  # if sign bit is set
            a = a - 0x100000000  # convert to negative

        return a     
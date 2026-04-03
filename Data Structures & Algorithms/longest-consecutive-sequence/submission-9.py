from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0

        for num in s:
            # start of a sequence
            if num - 1 not in s:
                length = 1
                cur = num
                while cur + 1 in s:
                    cur += 1
                    length += 1
                best = max(best, length)

        return best
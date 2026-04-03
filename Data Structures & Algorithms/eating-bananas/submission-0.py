from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l < r:
            k = (l + r) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p/k)

            if hours <= h:
                r = k      # k works, try smaller
            else:
                l = k + 1  # k too small, need bigger

        return l
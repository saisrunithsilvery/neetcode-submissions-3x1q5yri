from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()      # stores indices, nums[dq] is decreasing
        res = []
        l = 0

        for r in range(len(nums)):
            # 1) keep deque decreasing: pop smaller values from the back
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            # 2) remove indices that are out of the window (left side)
            if dq[0] < l:
                dq.popleft()

            # 3) when window size hits k, record max and slide left
            if r - l + 1 >= k:
                res.append(nums[dq[0]])
                l += 1

        return res
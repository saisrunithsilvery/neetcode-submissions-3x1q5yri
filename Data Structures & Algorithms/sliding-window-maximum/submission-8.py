from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()   # stores indices
        result = []

        l = 0

        for r in range(len(nums)):

            # Remove indices that are outside the current window
            while queue and queue[0] < l:
                queue.popleft()

            # Remove smaller values from the right
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()

            # Add current index
            queue.append(r)

            # When window size becomes k, record the max
            if r - l + 1 == k:
                result.append(nums[queue[0]])
                l += 1

        return result
from collections import defaultdict
from typing import List, Tuple

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)  # key -> List[(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        if not arr:
            return ""

        l, r = 0, len(arr) - 1
        ans = ""  # default if nothing <= timestamp

        while l <= r:
            mid = (l + r) // 2
            t, v = arr[mid]

            if t <= timestamp:
                ans = v          # this is a valid candidate
                l = mid + 1      # try to find a later one
            else:
                r = mid - 1      # go left

        return ans
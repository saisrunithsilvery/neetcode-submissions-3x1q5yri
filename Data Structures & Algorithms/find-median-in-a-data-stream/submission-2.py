import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap (negate values since Python only has min-heap)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # default: push to left (max-heap)
        heapq.heappush(self.small, -num)

        # make sure left top <= right top
        while self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # rebalance: sizes can differ by at most 1
        while len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        while len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2


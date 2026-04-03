import heapq  # typo: you had "heaphq"

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

        # trim the heap down to only k elements
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)  # was missing self.nums

        # if heap grew beyond k, remove the smallest
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)

        # the root of a size-k min-heap IS the kth largest
        return self.nums[0]
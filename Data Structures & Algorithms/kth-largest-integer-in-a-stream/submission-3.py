import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

        while len(self.nums) >= k :
            heapq.heappop(self.nums)



    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        kth_val = heapq.heappop(self.nums)
        return kth_val


        

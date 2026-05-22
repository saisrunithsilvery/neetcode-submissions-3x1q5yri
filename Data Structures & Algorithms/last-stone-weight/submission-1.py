import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = []
        for n in stones:
            heapq.heappush(max_heap, -n)

        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)

            if x != y:
                heapq.heappush(max_heap, x - y)

        return -max_heap[0] if max_heap else 0
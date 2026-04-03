class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        from typing import List
        heap = []
        for x, y in points:
            d = x*x + y*y
            heapq.heappush(heap, (d, x, y))

        ans = []
        for _ in range(k):
            _, x, y = heapq.heappop(heap)
            ans.append([x, y])
        return ans
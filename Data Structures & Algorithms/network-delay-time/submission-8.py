import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashmap = defaultdict(list)
        for ui, vi, ti in times:
            hashmap[ui].append((ti, vi))

        heap = [(0, k)]
        visit = set()

        while heap:
            distance, node = heapq.heappop(heap)

            if node in visit:          # stale entry, already finalized
                continue
            visit.add(node)            # finalize on pop

            if len(visit) == n:        # last node finalized = max shortest path
                return distance

            for t, v in hashmap[node]:
                if v not in visit:
                    heapq.heappush(heap, (distance + t, v))

        return -1
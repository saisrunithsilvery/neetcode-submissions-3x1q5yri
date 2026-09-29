import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        if len(times) != n:
            return -1

        graph = defaultdict(list)

        for u, v, time in times:
            graph[u].append((v, time))

        heap = [(0, k)]
        visit = set()

        while heap:
            time, node = heapq.heappop(heap)

            if node in visit:

                continue

            visit.add(node)

            for nei, weight in graph[node]:
                if nei not in visit:
                    heapq.heappush(heap, (time + weight, nei))

        return time-1         














        

    
        
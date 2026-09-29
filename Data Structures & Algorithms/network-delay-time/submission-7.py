import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        
        graph = defaultdict(list)

        for u, v, time in times:
            graph[u].append((v, time))

        heap = [(0, k)]
        visit = set()
        max_time = 0

        while heap:
            time, node = heapq.heappop(heap)
            if node in visit:
                continue

            visit.add(node)
            max_time = time

            for nei, weight in graph[node]:
                if nei not in visit:
                    heapq.heappush(heap, (time + weight, nei))
        if len(visit) != n:
            return -1
            

        return max_time















        

    
        
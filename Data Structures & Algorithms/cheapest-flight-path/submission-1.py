import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = defaultdict(list)
        for i, j, price in flights:
            graph[i].append([j, price])
        heap = []
        for j, price in graph[src]:
            heapq.heappush(heap, [price, 0,  src, j])

        while heap:
            price, st, src, des = heapq.heappop(heap)

            if des == dst and st <= k:
                return price
            if st > k:
                continue    

            graph[0] = [edge for edge in graph[0] if edge[0] != des]
            for j, price1 in graph[des]:
                heapq.heappush(heap, [price + price1,st+1, des, j])
                    
        return -1

        


        
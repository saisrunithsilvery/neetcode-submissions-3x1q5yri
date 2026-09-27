import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]   # negate
        heapq.heapify(stones) 

        while stones and len(stones) > 1:

            st1 = -1*(heapq.heappop(stones))
            st2 = -1*(heapq.heappop(stones))

            nw_wight = abs(st1 - st2)

            if nw_wight != 0:
                heapq.heappush(stones, -1*nw_wight)


        return -1*(stones[0]) if stones else 0        



    
        
from collections import Counter
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        hashset = Counter(tasks)

        maxHeap = [-count for count in hashset.values()]
        heapq.heapify(maxHeap)


        q = deque()
        time = 0

        while maxHeap or q :

            time +=1

            if maxHeap:
                count = heapq.heappop(maxHeap)
                count +=1

                if count != 0:
                    q.append([count, time+n])

            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time                 





        




        
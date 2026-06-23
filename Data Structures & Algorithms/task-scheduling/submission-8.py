from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq = Counter(tasks)

        # max heap using negative counts
        maxHeap = [-count for count in freq.values()]
        heapq.heapify(maxHeap)

        # queue stores: [remaining_count, available_time]
        q = deque()

        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                count = heapq.heappop(maxHeap)
                count += 1   # because count is negative

                if count != 0:
                    q.append([count, time + n])

            # if cooldown finished, push back to heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
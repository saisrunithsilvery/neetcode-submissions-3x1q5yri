"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        heap = []

        count = 0
        n = len(intervals)
        for i in range(n):

            if not heap:
                count +=1
                heapq.heappush(heap, intervals[i].end)

            elif heap[0] < intervals[i].start:
                heapq.heappop(heap)    
                heapq.heappush(heap, intervals[i].end)
            else:
                heapq.heappush(heap, intervals[i].end )
                count +=1
        return count            


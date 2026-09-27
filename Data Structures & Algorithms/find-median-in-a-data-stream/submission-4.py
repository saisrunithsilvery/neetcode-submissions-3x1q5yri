
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:

        heapq.heappush(self.max_heap, (-1)*num)

        if  self.min_heap :

            if (-1)*self.max_heap[0] > self.min_heap[0]:
                x = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, -1*x)

        if len(self.max_heap) > len(self.min_heap) + 1:

            x = heapq.heappop(self.max_heap)

            heapq.heappush(self.min_heap, -x)        


        elif len(self.min_heap) > len(self.max_heap):

            x = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -1*x)
        

    def findMedian(self) -> float:

        # Odd number of elements
        if len(self.max_heap) > len(self.min_heap):

            return float(-self.max_heap[0])

        # Even number of elements
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0

        
        


        
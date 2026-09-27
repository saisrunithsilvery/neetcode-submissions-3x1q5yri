class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        heap = []

        for index, point in enumerate(points):

            distance = (point[0]**2) + (point[1]**2)
            
            heapq.heappush(heap, (-1*distance, index, point[0], point[1]))

            while len(heap) > k :
                heapq.heappop(heap)

        result = []        

        while heap :
            dist, i, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result    
            

    


        
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        degree = [0]*numCourses
        result = []

        for course, pre in prerequisites:
            graph[pre].append(course)
            degree[course] +=1
    

        q = deque()

        for i in range(numCourses):
            if degree[i]==0:
                q.append(i)
                result.append(i)

        if not q:
            return []        

        while q:
            x = q.popleft()

            for j in graph[x]:
                degree[j] -=1

                if degree[j] == 0:
                    q.append(j)
                    result.append(j)

        return result if len(result) == numCourses else []           


            
        
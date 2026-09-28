from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        degree = [0] * numCourses
        courses_dep = defaultdict(list)
        for crs, pre in prerequisites:
            courses_dep[pre].append(crs)
            degree[crs] += 1
        q = deque()
        
        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)

        while q:
            crs = q.popleft()
            result.append(crs)

            # Courses that depend on this completed course
            for dep in courses_dep[crs]:
                degree[dep] -= 1

                # All prerequisites for dep are completed
                if degree[dep] == 0:
                    q.append(dep)

        # If we processed every course, valid ordering exists
        if len(result) == numCourses:
            return result

        # Otherwise there is a cycle
        return []
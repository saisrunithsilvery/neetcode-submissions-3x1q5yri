class Solution:
    def canFinish(self, numCourses, prerequisites):
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)
        visit = set()
        def dfs(crs):

            if crs in  visit :
                return False 

            if premap[crs] == []:
                return True
            visit.add(crs)    
            for i in premap[crs]:
                if not dfs(i):
                    return False
            visit.remove(crs)
            premap[crs] =[]
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True        



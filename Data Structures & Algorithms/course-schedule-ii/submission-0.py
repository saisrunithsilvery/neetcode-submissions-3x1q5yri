class Solution:
    def findOrder(self, numCourses, prerequisites):
        premap = defaultdict(list)
        for crs, pre in prerequisites:
            premap[crs].append(pre)

        visit = set()
        done = set()
        result = []

        def dfs(crs):
            if crs in visit:
                return False
            if crs in done:
                return True
            visit.add(crs)

            for i in premap[crs]:
                if not dfs(i):
                    return False

            visit.remove(crs)
            done.add(crs)
            result.append(crs)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if not edges:
            return 0 
        result = 0
        visited = set() 
        map1 = defaultdict(list)
        for i , j in edges:
            map1[i].append(j)
            map1[j].append(i)

        def dfs(x):

            if x in visited:
                return
            visited.add(x)
            for i in map1[x]:
                dfs(i)    

        for i in map1.keys():

            if i in visited:
                continue
            else:
                result +=1
                dfs(i)

        return result + n - len(map1)           

        
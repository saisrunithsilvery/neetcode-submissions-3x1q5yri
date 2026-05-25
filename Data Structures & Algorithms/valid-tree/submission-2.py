from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n != len(edges) + 1 :
            return False
        
        if not edges:
            return True    

        map1 = defaultdict(list)

        for i, j in edges :

            map1[i].append(j)
            map1[j].append(i)

        def bfs(k):

            q = deque()
            visited = set()
            q.append(k)
            while q :
                x = q.pop()
                visited.add(x)
                for i in map1[x] :
                    if i not in visited:
                        q.append(i)
                    


            if len(visited) < n:
                return False
            else:
                return True    
        if not bfs(edges[0][0]):
            return False
        return True                    
        


        
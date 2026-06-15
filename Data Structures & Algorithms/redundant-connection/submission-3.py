class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1]*(n + 1)
        parent = [i for i in range(n+1)]


        def find(node1):
            if parent[node1] != node1:
                parent[node1] = find(parent[node1])  # Path compression
            return parent[node1]

        def union(a, b):
            p1, p2 = find(a), find(b)
            if p1 == p2:
                return True

            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
                rank[p2] = 0
            else:
                parent[p1] = p2    
                rank[p2] += rank[p1]
                rank[p1] = 0
            return False    
                   

        for edge in edges:

            if union(edge[0], edge[1]):
                return list(edge)







        
        
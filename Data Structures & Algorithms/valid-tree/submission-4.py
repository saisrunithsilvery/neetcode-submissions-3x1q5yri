class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:


        parents = [i for i in range(n)]
        rank = [1]*n
        



        def find(node):

            parent = parents[node]
            if node == parent:
                return parent
            return find(parent)

        def union(u, v):

            p1, p2 = find(u), find(v)

            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                rank[p1] += rank[p2]
                rank[p2] = 0
                parents[p2] = p1
            else:
                rank[p2] += rank[p1]
                rank[p1] = 0
                parents[p1] = p2

            return True    

        for u, v in edges:
            if not union(u, v):
                return False

        if len(edges) != n - 1:
            return False

        return True    







        







        

        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parents = [i for i in range(n)]
        size = [1] * n

        def find(node):
            if node != parents[node]:
                parents[node] = find(parents[node])
            return parents[node]

        def union(u, v):
            p1 = find(u)
            p2 = find(v)

            if p1 == p2:
                return False

            if size[p1] >= size[p2]:
                parents[p2] = p1
                size[p1] += size[p2]
            else:
                parents[p1] = p2
                size[p2] += size[p1]

            return True

        components = n

        for u, v in edges:
            if union(u, v):
                components -= 1

        return components
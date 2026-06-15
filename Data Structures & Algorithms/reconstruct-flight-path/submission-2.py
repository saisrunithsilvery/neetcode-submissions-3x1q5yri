from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src, dst in tickets:
            graph[src].append(dst)
        
        for key in graph:
            graph[key].sort()
        
        res = []
        
        def dfs(src):
            while graph[src]:
                dst = graph[src].pop(0)  # Remove edge, iterate correctly
                dfs(dst)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]
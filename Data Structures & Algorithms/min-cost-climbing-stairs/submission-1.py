class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        mem = [-1]*(n+1)
        cost.append(0)


        def td(x):

            if  x < 0 :
                return 0

            if x==0:
                return cost[0]    

            if mem[x] != -1:
                return mem[x]

            mem[x] = cost[x]+min(td(x-1), td(x-2)) 

            return mem[x]

        return td(n)

        


            
        
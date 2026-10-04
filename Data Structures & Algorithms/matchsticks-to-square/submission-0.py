class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        sides = [0,0,0,0]

        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total//4  


        def backtacking(index):

            if index == len(matchsticks):
                return True

            val = matchsticks[index]

            for i in range(4):
                if sides[i]+val <= target:

                    sides[i] += val
                    if backtacking(index+1):
                        return True

                    sides[i] -= val
            return False

        return backtacking(0)
                    



        
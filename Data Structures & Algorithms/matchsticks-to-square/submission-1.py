class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        # Try large sticks first
        matchsticks.sort(reverse=True)

        # If largest stick itself is too large
        if matchsticks[0] > target:
            return False

        sides = [0, 0, 0, 0]

        def backtracking(index):

            if index == len(matchsticks):
                return True

            val = matchsticks[index]

            for i in range(4):

                # Don't exceed target
                if sides[i] + val > target:
                    continue

                # Don't try equivalent sides
                if i > 0 and sides[i] == sides[i - 1]:
                    continue

                sides[i] += val

                if backtracking(index + 1):
                    return True

                sides[i] -= val

            return False

        return backtracking(0)
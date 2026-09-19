class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = sorted(zip(position, speed))
        fleets = 0

        last_time = -1


        for pos, spd in reversed(pairs):

            time = (target- pos)/spd

            if time > last_time:
                fleets +=1
                last_time = time

        return fleets    

        
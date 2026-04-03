class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)  # by position desc
        fleets = 0
        max_time = 0

        for pos, spd in cars:
            t = (target - pos) / spd
            if t > max_time:
                fleets += 1
                max_time = t
            # else: merges into existing fleet

        return fleets
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        results = [intervals[0]]

        for i in range(1, len(intervals)):
            last = results[-1]
            curr = intervals[i]

            # Overlapping intervals
            if last[1] >= curr[0]:
                last[1] = max(last[1], curr[1])
            else:
                results.append(curr)

        return results

        
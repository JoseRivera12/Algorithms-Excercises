class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i = 0
        res = []

        # no overlapping intervals
        while i < n and newInterval[0] > intervals[i][1]:
            res.append(intervals[i])      
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[1] = max(intervals[i][1], newInterval[1])
            newInterval[0] = min(intervals[i][0], newInterval[0])
            i += 1
        res.append(newInterval)

        # no overlapping rest
        while i < n:
            res.append(intervals[i])
            i += 1

        return res

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # intervals.sort(key=lambda x:x[0])
        
        # last = float('-inf')
        # for meeting in intervals:
        #     start, end = meeting
        #     if last > start:
        #         return False
        #     last = end
        
        # return True
        # without auxiliar var
        intervals.sort(key=lambda x:x[0])
        for i in range(len(intervals) - 1):
            if intervals[i + 1][0] < intervals[i][1]:
                return False
        
        return True
